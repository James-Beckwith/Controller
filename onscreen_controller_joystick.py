from tkinter import *

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
        rad = 0.5 * (oval_coords[2] - oval_coords[0])
        cent = oval_coords[0] + rad, oval_coords[1] + rad
        point_dist = ((cent[0] - x) ** 2 + (cent[1] - y) ** 2) ** 0.5
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
oval_coords = 100, 100, 380, 380
oval = C.create_oval(oval_coords, fill="blue")

window.bind('<Motion>', motion) # reacts to motion, function tracks cursor position
window.bind('<Button-1>', set_flag) # only start car when left mouse is clicked
window.bind('<ButtonRelease-1>',unset_flag) # stop car when left mouse button unclicked

#window.Framepack()
window.resizable(width=False, height=False)
# run infinite loop for window. window will wait for user input until it is closed
window.mainloop()
