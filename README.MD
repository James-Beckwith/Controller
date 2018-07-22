# Amazing fast and autonomous car powered by a Raspberry Pi 

 - https://github.com/James-Beckwith/Controllerhttps://github.com/James-Beckwith/Controller

## VNC
### On the server
 - x11vnc -storepasswd .vncpassword
 - x11vnc -auth guess -forever -loop -noxdamage -repeat -rfbauth .vncpassword -rfbport 5900 -shared

### On the viewer
 - Install vncviewer


## Settings for Python
 * Tested with python 3.5 (GG) and 3.6 (JB)
 * Require
	- sudo apt-get install  python3-tk (graphical interf)
	-  sudo apt-get install python3-pil python3-pil.imagetk (import images)


## TODO
	* Local path to the image
	* Short documentation
	* Normalize printed values between -1 and 1

	* In file with image:
	 	- replace line 59/60 by

			. img = ImageTk.PhotoImage(file="./analog_stick_1x_small.png")
			. Cimg = C.create_image(300,300,image=img,anchor='nw')

		- but I loose the size of the image...


1. The screen size was bigger than my phone screen so I had to scroll along the window with phone, this was difficult and will cause problems.
Let me know
	- I think this problem can be solved by making the window size as big as the screen. This will prevent user from modifying the raspberry pi setting (i.e. the will access only the python window)...	
	- Discovered another problem: it's not easy no click on a tactile screen... Maybe trigger event when the finger go over the screen. We can talk about this tomorrow.

2. I want the controller program to start up automatically when I log into the VNC.  I didn't manage to do this, although I only spent 2 minutes trying to do it. I currently just have a shell script on the desktop that I double click to start the program
 	- https://serverfault.com/questions/639926/ubuntu-run-a-command-when-vnc-session-starts (Does not work for me, so such file as .vncstartup)

3. Can we limit the VNC connection to one person at a time. If multiple people are connected then how does this affect the controls?
	No solution found...	
	- https://ubuntuforums.org/archive/index.php/t-1472471.html
	- http://www.karlrunge.com/x11vnc/x11vnc_opts.html (X11VNC_CREATE_MAX_DISPLAYS=n) 
	


