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

# Deinfe a function to run when button is clicked
def chicken(event):
    print('cluck')
def dog(event):
    print('woof')

window.title("Controller")
window.geometry('800x400') # set window size

# Add a label
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

## Add a button
btn = Button(window, text="Click Me",command=chicken)
btn.grid(column=1, row=0)

btn2 = Button(window, text="test")
btn2.grid(column=2, row=0)
btn2.bind('<Button-1>',chicken)
btn2.bind('<ButtonRelease-1>',dog)
#btn2 = Custom_button(window,text = 'Press ')
#btn2.set_up(dog)
#btn2.set_down(chicken)
#btn2.grid(column=2,row=0)
#btn.pack()

# run infinite loop for window. window will wait for user input until it is closed
window.mainloop()
