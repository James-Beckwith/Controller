# Note, we require both tkinter and PIL to be installed

from tkinter import * # for creating window
from PIL import Image, ImageTk # for managing images
import math
# setup GPIO for controlling motors
import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

# define root window
window = Tk()

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
# NOTE: A = left, B = right
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# How many times to turn the pin on and off each second
Frequency = 20

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(0)
pwmMotorABackwards.start(0)
pwmMotorBForwards.start(0)
pwmMotorBBackwards.start(0)

#initialise flag, used to control start - may be redundant
flag=0

#define function to update motors
def updateMotors(rad,pointDist,dx,dy):
    # define contribution ot forward, reverse, left right
    speed = 100 * pointDist / rad
    ang = atan2(y,x) # angle is measured from positive x direction in radians
    if (dx < 0): # going left
        speedLeft = speed
        speedRight = speed * (math.pi - math.fabs(ang)) / (math.pi / 2)
    else: # going right
        speedRight = speed
        speedLeft = speed * (math.pi - math.fabs(ang)) / (math.pi / 2)
    # set motor values accordingly
    if (dy < 0): # going backwards
        pwmMotorAForwards.ChangeDutyCycle(speedLeft)
        pwmMotorABackwards.ChangeDutyCycle(0)
        pwmMotorBForwards.ChangeDutyCycle(0)
        pwmMotorBBackwards.ChangeDutyCycle(speedRight)
    else: # going forwards
        pwmMotorAForwards.ChangeDutyCycle(speedLeft)
        pwmMotorABackwards.ChangeDutyCycle(0)
        pwmMotorBForwards.ChangeDutyCycle(speedRight)
        pwmMotorBBackwards.ChangeDutyCycle(0)
# Deinfe a function to run when button is clicked
def motion(event):
    if (flag==1):
        x, y = event.x, event.y
        #check if current point is within oval
        global imgCent
        rad = 0.5 * img.width() # Note, I am assuming a square image#
        dx = (imgCent[0] - x)
        dy = (imgCent[1] - y)
        pointDist = (dx ** 2 + dy ** 2) ** 0.5
        # if cursor is within current window, do something
        if (pointDist<rad):
            print('{}, {}'.format(x, y))
            # change motors given on update cursor location
            updateMotors(rad,pointDist,dx,dy)
def setFlag(event): # after button is pressed, allow movement to control car
    global flag
    flag=1
def unsetFlag(event): # stop motors if button is released
    global flag
    global pwmMotorAForwards, pwmMotorBForwards, pwmMotorABackwards, pwmMotorBBackwards
    flag=0
    # stop mtors
    pwmMotorAForwards.start(Stop)
    pwmMotorABackwards.start(Stop)
    pwmMotorBForwards.start(Stop)
    pwmMotorBBackwards.start(Stop)

# create window
window.title("Controller")
window.resizable(width=False, height=False) # make window a fixed size
# set window size
window.geometry('400x400')

# start a canvas in which to put the image
C = Canvas(window, bg="white", height=400, width=400)
C.pack()

# will need to replace path to image file with whatever image you want!
img = ImageTk.PhotoImage(file="/home/pi/python_scripts/controls/Controller/analog-stick.png")
img_cent = 200, 200 # define image centre point in pixels
Cimg = C.create_image(img_cent[0],img_cent[1], image=img) # add image

# define actionns to take when movement or certain button clicks are recognised
window.bind('<Motion>', motion) # reacts to motion, function tracks cursor position
window.bind('<Button-1>', set_flag) # only start car when left mouse is clicked
window.bind('<ButtonRelease-1>',unset_flag) # stop car when left mouse button unclicked

#window.Framepack()
window.resizable(width=False, height=False)
# run infinite loop for window. window will wait for user input until it is closed
window.mainloop()
