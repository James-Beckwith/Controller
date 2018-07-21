# Note, we require both tkinter and PIL to be installed

from tkinter import *
from PIL import Image, ImageTk

# define root window
window = Tk()

# #define custom button classs
# class Custom_button(Button):
#     # set function to call when pressed
#     def set_down(self,fn):
#         self.bind('<Button-1>',fn)
#
#     # set function to be called when released
#     def set_up(self,fn):
#         self.bind('<ButtonRelease-1>',fn)
#

#pack frame into window
#frame = Frame(window)
#frame.pack()

#initialise flag
flag=0

# Deinfe a function to run when button is clicked
def motion(event):
    if (flag==1):
        x, y = event.x, event.y
        #check if current point is within oval
        global oval_coords
        rad = 0.5 * (img.width()) # Note, I am assuming a square image
        point_dist = ((img_cent[0] - x) ** 2 + (img_cent[1] - y) ** 2) ** 0.5
        # if cursor is within current window, do something
        if (point_dist<rad):
            print('{}, {}'.format(x, y))
def set_flag(event):
    global flag
    flag=1
def unset_flag(event):
    global flag
    flag=0

window.title("Controller")
window.resizable(width=False, height=False)
#root.geometry('{}x{}'.format(<widthpixels>, <heightpixels>))
window.geometry('400x400')

C = Canvas(window, bg="white", height=400, width=400)
C.pack()

#window.create_oval(x0, y0, x1, y1, option, ...)
#oval_coords = 100, 100, 380, 380
#oval = C.create_oval(oval_coords, fill="blue")

# will need to replace path to image file with whatever image you want!
img = ImageTk.PhotoImage(file="/home/pi/python_scripts/controls/Controller/analog-stick.png")
img_cent = 200, 200
Cimg = C.create_image(img_cent[0],img_cent[1], image=img)
#btn = Button(window, image=img)
#btn_fwd.grid(column=1, row=0)
#btn_fwd.bind('<Button-1>',fwd_on)
#btn_fwd.bind('<ButtonRelease-1>',fwd_off)
#btn_fwd.pack(side=TOP)

window.bind('<Motion>', motion) # reacts to motion, function tracks cursor position
window.bind('<Button-1>', set_flag) # only start car when left mouse is clicked
window.bind('<ButtonRelease-1>',unset_flag) # stop car when left mouse button unclicked

#window.Framepack()
window.resizable(width=False, height=False)
# run infinite loop for window. window will wait for user input until it is closed
window.mainloop()
