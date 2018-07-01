from tkinter import *

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

frame = Frame(window)
frame.pack()

# Deinfe a function to run when button is clicked
def left_on(event):
    print('Put some stuff here')
def left_off(event):
    print('Put some stuff here')
def right_on(event):
    print('Put some stuff here')
def right_off(event):
    print('Put some stuff here')
def fwd_on(event):
    print('Put some stuff here')
def fwd_off(event):
    print('Put some stuff here')
def rev_on(event):
    print('Put some stuff here')
def rev_off(event):
    print('Put some stuff here')

window.title("Controller")
#window.geometry('800x400') # set window size

# Add a label
#lbl = Label(window, text="Hello")
#lbl.grid(column=0, row=0)

# add buttons and bind button press and release to different functions
#add left button
btn_left = Button(frame, text="Left", font=("Arial Bold", 50))
#btn_left.grid(column=0, row=1)
btn_left.bind('<Button-1>',left_on)
btn_left.bind('<ButtonRelease-1>',left_off)
btn_left.pack(side=LEFT)

#add right button
btn_right = Button(frame, text="Right", font=("Arial Bold", 50))
#btn_right.grid(column=2, row=1)
btn_right.bind('<Button-1>',right_on)
btn_right.bind('<ButtonRelease-1>',right_off)
btn_right.pack(side=RIGHT)

#add right button
btn_fwd = Button(frame, text="Forward", font=("Arial Bold", 50))
#btn_fwd.grid(column=1, row=0)
btn_fwd.bind('<Button-1>',fwd_on)
btn_fwd.bind('<ButtonRelease-1>',fwd_off)
btn_fwd.pack(side=TOP)

#add right button
btn_rev = Button(frame, text="Reverse", font=("Arial Bold", 50))
#btn_rev.grid(column=1, row=2)
btn_rev.bind('<Button-1>',rev_on)
btn_rev.bind('<ButtonRelease-1>',rev_off)
btn_rev.pack(side=BOTTOM)

#window.Framepack()
# run infinite loop for window. window will wait for user input until it is closed
window.mainloop()
