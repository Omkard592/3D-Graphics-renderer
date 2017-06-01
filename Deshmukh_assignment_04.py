# Deshmukh, Omkar
# 1001-275-806
# 2015-04-20
# Assignment_04

###################################################################################################################################### 
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

import string

from Deshmukh_widgets_04 import *
from Deshmukh_graphics_04 import *
from Deshmukh_camera_04 import *

def close_window_callback(root):    #define a closing action
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

ob_root_window = Tk()   #create a Tk object (window)
ob_root_window.wm_title("Omkar Deshmukh - 1001275806 Assg 4")
#define window protocol
ob_root_window.protocol("WM_DELETE_WINDOW", lambda root_window=ob_root_window: close_window_callback(root_window))
cam=cl_camera()
ob_world=cl_world()     #create a graphics class object
cl_widgets(ob_root_window,cam,ob_world)     #pass window and graphics class objects to widgets class constructor
ob_root_window.mainloop()   #to keep the main window alive as long as events appear
###################################################################################################################################### 