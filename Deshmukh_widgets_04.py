# Deshmukh, Omkar
# 1001-275-806
# 2015-04-20
# Assignment_04

###################################################################################################################################### 
from tkinter import *
from math import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

from PIL import ImageTk, Image, ImageDraw

import math
import copy
import numpy as NP

class cl_widgets:
    
    def __init__(self,ob_root_window,camera,ob_world=[]):      #takes a TK window obj and graphics class obj
        #print("CL WIDGETS")
        self.ob_root_window=ob_root_window
        self.ob_world=ob_world
        self.camera=camera
        #self.menu=cl_menu(self)
        #self.toolbar=cl_toolbar(self)
        #self.pannel_01 = cl_pannel_01(self)
        self.pannel_02 = cl_pannel_02(self)
        self.pannel_03 = cl_pannel_03(self)
        self.pannel_04 = cl_pannel_04(self)
        self.pannel_05 = cl_pannel_05(self)
        self.pannel_06 = cl_pannel_06(self)
        self.ob_canvas_frame=cl_canvas_frame(self)
        #self.status = cl_statusBar_frame(self)
        self.ob_world.add_canvas(self.ob_canvas_frame.canvas)
        self.vert=[[]]
        
class cl_canvas_frame:
    
    def __init__(self, master):
        #print("CL CANVAS FRAME")
        self.master=master
        self.canvas = Canvas(master.ob_root_window,width=640, height=640, bg="yellow", highlightthickness=0)
        self.canvas.pack(expand=YES, fill=BOTH) 
        self.canvas.bind('<Configure>', self.canvas_resized_callback) 
        self.canvas.bind("<ButtonPress-1>", self.left_mouse_click_callback)
        #self.canvas.bind("<ButtonRelease-1>", self.left_mouse_release_callback)
        #self.canvas.bind("<B1-Motion>", self.left_mouse_down_motion_callback)
        #self.canvas.bind("<ButtonPress-3>", self.right_mouse_click_callback)
        #self.canvas.bind("<ButtonRelease-3>", self.right_mouse_release_callback)
        #self.canvas.bind("<B3-Motion>", self.right_mouse_down_motion_callback)
        #self.canvas.bind("<Key>", self.key_pressed_callback)    
        self.canvas.bind("<Up>", self.up_arrow_pressed_callback)
        self.canvas.bind("<Down>", self.down_arrow_pressed_callback)
        self.canvas.bind("<Right>", self.right_arrow_pressed_callback)
        self.canvas.bind("<Left>", self.left_arrow_pressed_callback)     
        self.canvas.bind("<Shift-Up>", self.shift_up_arrow_pressed_callback)
        self.canvas.bind("<Shift-Down>", self.shift_down_arrow_pressed_callback)
        self.canvas.bind("<Shift-Right>", self.shift_right_arrow_pressed_callback)
        self.canvas.bind("<Shift-Left>", self.shift_left_arrow_pressed_callback)   
        self.canvas.bind("f", self.f_key_pressed_callback)  
        self.canvas.bind("b", self.b_key_pressed_callback)
        self.master.ob_world.draw_camera_frames(self.canvas,self.master.camera.name,self.master.camera.view)
        
    def key_pressed_callback(self,event):
        print ('key pressed')      
        
    def up_arrow_pressed_callback(self,event):
        print ('pressed up')
        
    def down_arrow_pressed_callback(self,event):
        print ('pressed down')     
        
    def right_arrow_pressed_callback(self,event):
        print ('pressed right')       
        
    def left_arrow_pressed_callback(self,event):
        print ('pressed left')    
        
    def shift_up_arrow_pressed_callback(self,event):
        self.canvas.world.translate(0,.1,0,1)
        
    def shift_down_arrow_pressed_callback(self,event):
        pass
    
    def shift_right_arrow_pressed_callback(self,event):
        pass
    
    def shift_left_arrow_pressed_callback(self,event):
        pass
    
    def f_key_pressed_callback(self,event):
        print ("f key was pressed")
        
    def b_key_pressed_callback(self,event):
        print ("b key was pressed")  
        
    def left_mouse_click_callback(self,event):
        print ('Left mouse button was clicked')
        print ('x=',event.x, '   y=',event.y)        
        self.x = event.x
        self.y = event.y  
        self.canvas.focus_set()
        
    def left_mouse_release_callback(self,event):
        print ('Left mouse button was released')
        print ('x=',event.x, '   y=',event.y)
        print ('canvas width', self.canvas.cget("width"))
        self.x = None
        self.y = None
        
    def left_mouse_down_motion_callback(self,event):
        print ('Left mouse down motion')
        print ('x=',event.x, '   y=',event.y)
        self.x = event.x
        self.y = event.y 
        
    def right_mouse_click_callback(self,event):
        self.x = event.x
        self.y = event.y   
        
    def right_mouse_release_callback(self,event):
        self.x = None
        self.y = None    
        
    def right_mouse_down_motion_callback(self,event):
        pass
    
    def canvas_resized_callback(self,event):
        #wsf = float(event.width)/self.width
        #hsf = float(event.height)/self.height
        self.canvas.config(width=event.width,height=event.height)
        #self.scale("all",0,50,wsf,hsf)
        #self.canvas.config(width=event.width-4,height=event.height-4)
        #print 'canvas width height', self.canvas.cget("width"), self.canvas.cget("height")
        #print 'event width height',event.width, event.height
        self.canvas.pack()
        #print ('canvas width', self.canvas.cget("width"))
        #print ('canvas height', self.canvas.cget("height"))
        '''self.master.ob_world.redisplay(self.master.ob_canvas_frame.canvas,event,
                                       self.master.pannel_02.faceslen,
                                       self.master.vert,
                                       self.master.pannel_02.faces,
                                       self.master.pannel_02.window,
                                       self.master.pannel_02.view)'''
        
        self.master.ob_world.redisplay(self.master.ob_canvas_frame.canvas,event,
                                       self.master.pannel_02.faceslen,
                                       self.master.camera.camcount,
                                       self.master.vert,
                                       self.master.pannel_02.faces,
                                       self.master.camera.window,
                                       self.master.camera.view)
        
        #self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.faceslen,1,self.master.camera.camcount,self.master.camera.name,self.master.camera.proj,self.master.camera.vrp,self.master.camera.vpn
        #    ,self.master.camera.vup,self.master.camera.prp,self.vertices,
        #                                  self.faces,self.master.camera.window,self.master.camera.view)
                                          
        #def draw_figures(self,canvas,faceslen,steps,camcount,xname=[],xproj=[],xvrp=[[]],xvpn=[[]],xvup=[[]],xprp=[[]],v=[[]],f=[[]],xw=[[]],xs=[[]]):
######################################################################################################################################		

######################################################################################################################################	
class cl_pannel_02():
    
    def __init__(self, master):
        #print("CP2")
        self.master=master
        self.var_filename = StringVar()
        self.var_filename.set('')
        self.filename=""
        frame = Frame(master.ob_root_window)
        frame.pack()
        
        self.labelText=StringVar()
        self.labelText.set("Filename:")
        self.labelDir=Label(frame, textvariable=self.labelText)
        self.labelDir.pack(side="left")

        
        self.dirname=Entry(frame,width=75)
        self.dirname.pack(side="left")        
        
        self.file_dialog_button = Button(frame, text="Browse", fg="blue", command=self.browse_file)
        self.file_dialog_button.pack(side="left") 
        #self.button = Button(frame, text="Open Dialog", fg="blue", command=self.open_dialog_callback)
        #self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Load", fg="red", command=self.button2_callback)
        self.hi_there.pack(side="left")
        self.vertices=[[]]
        self.faces=[[]]
        self.window=[]
        self.view=[]
        self.faceslen=0
        self.vi=0
        self.fi=0
        
    '''def open_dialog_callback(self):
        d = MyDialog(self.master.ob_root_window)
        print ( d.result)
        print ( "mydialog_callback pressed!"   )'''     
        
    def browse_file(self):
        self.var_filename.set(filedialog.askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.txt")]))
        self.filename=self.var_filename.get()
        self.dirname.insert(0,self.filename)
        #labelDir
        #print(self.filename)

    def button2_callback(self):
        self.filename=self.master.pannel_02.filename
        self.vertices=[[]]
        self.faces=[[]]
        self.faceslen=0
        self.vi=0
        self.fi=0
        
        #print ("Load pressed!")
        with open(self.filename) as inp:
            inplines = inp.readlines()
        #print("")
        for line in inplines:
            if 'v' in line:
                line=line[2:]
                self.vertices[self.vi]=[float(a) for a in line.split()]
                self.vertices.append([])
                self.vi+=1
            if 'f' in line:
                line=line[2:]
                self.faces[self.fi]=[float(b) for b in line.split()]
                self.faces.append([])
                self.fi+=1
        
        self.vertices.pop()
        self.faces.pop()
        #print("load")
        #print(self.vertices)
        self.master.vert=copy.deepcopy(self.vertices)
        #print("master")
        #print(self.master.vert)
        self.faceslen=len(self.faces[0])
        
        
            
        self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.faceslen,1,self.master.camera.camcount,self.master.camera.name,self.master.camera.proj,self.master.camera.vrp,self.master.camera.vpn
            ,self.master.camera.vup,self.master.camera.prp,self.vertices,
                                          self.faces,self.master.camera.window,self.master.camera.view)
######################################################################################################################################
                                          
######################################################################################################################################
class cl_pannel_03():
    def __init__(self, master):
        #print("CP3")
        self.master=master
        self.f = Frame(self.master.ob_root_window)
        self.innerf = Frame(self.f)
        col=1
        
        self.labelText=StringVar()
        self.labelText.set("Rotation Axis: (Default=Z)")
        self.labelDir=Label(self.innerf, textvariable=self.labelText)
        self.labelDir.grid(row=1, column=col)
        col+=1

        axes = [("X", "1"), ("Y", "2"), ("Z", "3")]

        self.v = StringVar()
        self.v.set("3")         # default is Z
        
        for tx, ax in axes:
            b = Radiobutton(self.innerf,text=tx, variable=self.v, value=ax)
            b.grid(row=1, column=col)
            col+=1
            
        self.labelText1=StringVar()
        self.labelText1.set("Degree:")
        self.labelDir1=Label(self.innerf, textvariable=self.labelText1)
        self.labelDir1.grid(row=1, column=col)
        col+=1
        
        self.var = StringVar()
        self.var.set("90")
        self.w = Spinbox(self.innerf, from_=0, to=360, width=4, textvariable=self.var)
        self.w.grid(row=1, column=col)
        col+=1
        
        self.labelText2=StringVar()
        self.labelText2.set("Steps:")
        self.labelDir2=Label(self.innerf, textvariable=self.labelText2)
        self.labelDir2.grid(row=1, column=col)
        col+=1
        self.w1 = Spinbox(self.innerf, from_=0, to=10, width=3)
        self.w1.grid(row=1, column=col)
        col+=1
        
        self.rotbut = Button(self.innerf, text="Rotate", fg="blue", command=self.rotate_callback)
        self.rotbut.grid(row=1, column=col)
        col+=1
        
        self.innerf.pack(side="left")
        self.f.pack()
        
    def rotate_callback(self):
        selectedrot=self.v.get()
        rotdegree=float(self.var.get())
        rotsteps=int(self.w1.get())         #steps increment
        vv=self.master.vert
        
        if rotsteps<1:
            rotsteps=0

        stepdegree=rotdegree
        #stepdegree=rotdegree/rotsteps
        tempvv=copy.deepcopy(vv)
        
        #for j in range(rotsteps):       #steps not working!!! :(
        for i in range(len(vv)):    
            if selectedrot=="1":        #X
                vv[i][0]=tempvv[i][0]
                vv[i][1]=float((round(math.cos(math.radians(stepdegree)),5)*tempvv[i][1])-(round(math.sin(math.radians(stepdegree)),5)*tempvv[i][2]))
                vv[i][2]=float((round(math.sin(math.radians(stepdegree)),5)*tempvv[i][1])+(round(math.cos(math.radians(stepdegree)),5)*tempvv[i][2]))
            
            if selectedrot=="2":        #Y
                vv[i][0]=float((round(math.cos(math.radians(stepdegree)),5)*tempvv[i][0])+(round(math.sin(math.radians(stepdegree)),5)*tempvv[i][2]))
                vv[i][1]=tempvv[i][1]
                vv[i][2]=float(-1*((round(math.sin(math.radians(stepdegree)),5)*tempvv[i][0]))+(round(math.cos(math.radians(stepdegree)),5)*tempvv[i][2]))
                
            if selectedrot=="3":        #Z
                vv[i][0]=float((round(math.cos(math.radians(stepdegree)),5)*tempvv[i][0])-(round(math.sin(math.radians(stepdegree)),5)*tempvv[i][1]))
                vv[i][1]=float((round(math.sin(math.radians(stepdegree)),5)*tempvv[i][0])+(round(math.cos(math.radians(stepdegree)),5)*tempvv[i][1]))
                vv[i][2]=tempvv[i][2]
                
            tempvv[i]=copy.deepcopy(vv[i])
                
        self.master.vert=copy.deepcopy(tempvv)
        '''self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,self.master.pannel_02.vrp,self.master.pannel_02.vpn,self.master.pannel_02.vup,self.master.pannel_02.prp,tempvv,
                                          self.master.pannel_02.faces,self.master.pannel_02.window,self.master.pannel_02.view)
        
        
        def draw_figures(self,canvas,faceslen,steps,camcount,xname=[],xproj=[],xvrp=[[]],xvpn=[[]],xvup=[[]],xprp=[[]],v=[[]],f=[[]],xw=[[]],xs=[[]]):'''
            
        self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,self.master.camera.camcount,self.master.camera.name,self.master.camera.proj,self.master.camera.vrp,self.master.camera.vpn
            ,self.master.camera.vup,self.master.camera.prp,tempvv,
                                          self.master.pannel_02.faces,self.master.camera.window,self.master.camera.view)
                                          
        #self.master.ob_canvas_frame.canvas.after(50)        #set 50ms delay
######################################################################################################################################
     
######################################################################################################################################
class cl_pannel_04():
    def __init__(self, master):
        #print("CP4")
        self.master=master
        self.f = Frame(self.master.ob_root_window) 
        self.innerf = Frame(self.f)
        col=1
        
        self.labelText=StringVar()
        self.labelText.set("Scale Ratio: (Default=All)")
        self.labelDir=Label(self.innerf, textvariable=self.labelText)
        self.labelDir.grid(row=1, column=col)
        col+=1
        
        options = [("All", "1"), ("[Sx,Sy,Sz]:", "2")]

        self.v = StringVar()
        self.v.set("1")         #default scale All
        self.var = StringVar()
        
        self.var.set("0.25")

        for tx, ax in options:
            if col==3:
                self.w = Spinbox(self.innerf, from_=0, to=4, width=4, format="%.2f",increment=0.25, textvariable=self.var)
                self.w.grid(row=1, column=col)
                col+=1
            
            b = Radiobutton(self.innerf,text=tx, variable=self.v, value=ax)
            b.grid(row=1, column=col)
            col+=1
        
        self.evar1 = StringVar()
        self.evar2 = StringVar()
        self.evar3 = StringVar()
        self.evar1.set("1.0")
        self.evar2.set("1.0")
        self.evar3.set("1.0")
        self.sx=Entry(self.innerf,width=3, textvariable=self.evar1)
        self.sx.grid(row=1, column=col)
        col+=1
        self.sy=Entry(self.innerf,width=3, textvariable=self.evar2)
        self.sy.grid(row=1, column=col)
        col+=1
        self.sz=Entry(self.innerf,width=3, textvariable=self.evar3)
        self.sz.grid(row=1, column=col)
        col+=1
        
        
        self.labelText1=StringVar()
        self.labelText1.set("A")
        self.labelDir1=Label(self.innerf, textvariable=self.labelText1)
        self.labelDir1.grid(row=1, column=col)
        col+=1  
        
        self.avar1 = StringVar()
        self.avar2 = StringVar()
        self.avar3 = StringVar()
        self.avar1.set("0.0")
        self.avar2.set("0.0")
        self.avar3.set("0.0")
        self.sx=Entry(self.innerf,width=3, textvariable=self.avar1)
        self.sx.grid(row=1, column=col)
        col+=1
        self.sy=Entry(self.innerf,width=3, textvariable=self.avar2)
        self.sy.grid(row=1, column=col)
        col+=1
        self.sz=Entry(self.innerf,width=3, textvariable=self.avar3)
        self.sz.grid(row=1, column=col)
        col+=1
        
        self.labelText2=StringVar()
        self.labelText2.set("Steps:")
        self.labelDir2=Label(self.innerf, textvariable=self.labelText2)
        self.labelDir2.grid(row=1, column=col)
        col+=1
        self.w1 = Spinbox(self.innerf, from_=0, to=10, width=3)
        self.w1.grid(row=1, column=col)
        col+=1
        
        self.scalebut = Button(self.innerf, text="Scale", fg="blue", command=self.scale_callback)
        self.scalebut.grid(row=1, column=col)
        col+=1
        
        self.innerf.pack(side="left")
        self.f.pack()
        
    def scale_callback(self):
        #print(self.v.get())
        #print("scale")
        vv=self.master.vert
        tempvv=copy.deepcopy(vv)
        selectedscale=self.v.get()
        
        sx=0.0
        sy=0.0
        sz=0.0
        
        if selectedscale=="1":    #Scale All
            sx=sy=sz=float(self.var.get())
            #print(sx)
            #print(sy)
            #print(sz)
            
        if selectedscale=="2":
            sx=float(self.evar1.get())
            sy=float(self.evar2.get())
            sz=float(self.evar3.get())
            #print(sx)
            #print(sy)
            #print(sz)
            
        ax=float(self.avar1.get())
        ay=float(self.avar2.get())
        az=float(self.avar3.get())
        #print(ax)
        #print(ay)
        #print(az)
        
        scalesteps=int(self.w1.get())         #steps increment
        #print(scalesteps)
        tx=ax-vv[0][0]
        ty=ay-vv[0][1]
        tz=az-vv[0][2]
        
        #sx=1+float(sx/scalesteps)
        #sy=1+float(sy/scalesteps)
        #sz=1+float(sz/scalesteps)
        
        #for j in range(scalesteps):     #steps not working!!! :(
            #print(scalesteps)
        for i in range(len(vv)):
                
            vv[i][0]=(tempvv[i][0]*sx)+tx-(sx*tx)       #from Hearn And Baker pg421
            vv[i][1]=(tempvv[i][1]*sy)+ty-(sy*ty)
            vv[i][2]=(tempvv[i][2]*sz)+tz-(sz*tz)
            #vv[i][0]=tx+tempvv[i][0]
                #print(tx)
                #print(str(vv[i][0])+" "+str(vv[i][1])+" "+str(vv[i][2]))
            #vv[i][0]=float(sx*vv[i][0])
                #print(str(vv[i][0])+" "+str(vv[i][1])+" "+str(vv[i][2]))
            #vv[i][0]=vv[i][0]-tx
                #print(str(vv[i][0])+" "+str(vv[i][1])+" "+str(vv[i][2]))
            #vv[i][1]=ty+tempvv[i][1]
            #vv[i][1]=float(sy*vv[i][1])
            #vv[i][1]=vv[i][1]-ty
            #vv[i][2]=tz+tempvv[i][2]
            #vv[i][2]=float(sz*vv[i][2])
            #vv[i][2]=vv[i][2]-tz
            tempvv[i]=copy.deepcopy(vv[i])
                
        self.master.vert=copy.deepcopy(tempvv)
        '''self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,self.master.pannel_02.vrp,self.master.pannel_02.vpn,self.master.pannel_02.vup,self.master.pannel_02.prp,tempvv,
                                          self.master.pannel_02.faces,self.master.pannel_02.window,self.master.pannel_02.view)'''
        
        self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,self.master.camera.camcount,self.master.camera.name,self.master.camera.proj,self.master.camera.vrp,self.master.camera.vpn
            ,self.master.camera.vup,self.master.camera.prp,tempvv,
                                          self.master.pannel_02.faces,self.master.camera.window,self.master.camera.view)
        #self.master.ob_canvas_frame.canvas.after(50)        #set 50ms delay
######################################################################################################################################
 
######################################################################################################################################
class cl_pannel_05():
    def __init__(self, master):
        #print("CP5")
        self.master=master
        self.f = Frame(self.master.ob_root_window) 
        self.innerf = Frame(self.f)
        col=1
        
        self.labelText1=StringVar()
        self.labelText1.set("Translation ([dx,dy,dz]):")
        self.labelDir1=Label(self.innerf, textvariable=self.labelText1)
        self.labelDir1.grid(row=1, column=col)
        col+=1  
        
        self.avar1 = StringVar()
        self.avar2 = StringVar()
        self.avar3 = StringVar()
        self.avar1.set("10")
        self.avar2.set("10")
        self.avar3.set("10")
        self.tx=Entry(self.innerf,width=3, textvariable=self.avar1)
        self.tx.grid(row=1, column=col)
        col+=1
        self.ty=Entry(self.innerf,width=3, textvariable=self.avar2)
        self.ty.grid(row=1, column=col)
        col+=1
        self.tz=Entry(self.innerf,width=3, textvariable=self.avar3)
        self.tz.grid(row=1, column=col)
        col+=1
        
        self.labelText2=StringVar()
        self.labelText2.set("Steps:")
        self.labelDir2=Label(self.innerf, textvariable=self.labelText2)
        self.labelDir2.grid(row=1, column=col)
        col+=1
        self.w1 = Spinbox(self.innerf, from_=0, to=10, width=3)
        self.w1.grid(row=1, column=col)
        col+=1
        
        self.scalebut = Button(self.innerf, text="Translate", fg="blue", command=self.translate_callback)
        self.scalebut.grid(row=1, column=col)
        col+=1
        
        self.innerf.pack(side="left")
        self.f.pack()
        
    def translate_callback(self):
        #print(self.v.get())
        #print("scale")
        vv=self.master.vert
        tempvv=copy.deepcopy(vv)
        
        tx=float(self.avar1.get())
        ty=float(self.avar2.get())
        tz=float(self.avar3.get())
        
        scalesteps=int(self.w1.get())         #steps increment
        #print(scalesteps)
        
        
        #sx=1+float(sx/scalesteps)
        #sy=1+float(sy/scalesteps)
        #sz=1+float(sz/scalesteps)
        
        #for j in range(scalesteps):     #steps not working!!! :(
            #print(scalesteps)
        for i in range(len(vv)):
                
            vv[i][0]=tempvv[i][0]+tx
            vv[i][1]=tempvv[i][1]+ty
            vv[i][2]=tempvv[i][2]+tz
            #vv[i][0]=tx+tempvv[i][0]
                #print(tx)
                #print(str(vv[i][0])+" "+str(vv[i][1])+" "+str(vv[i][2]))
            #vv[i][0]=float(sx*vv[i][0])
                #print(str(vv[i][0])+" "+str(vv[i][1])+" "+str(vv[i][2]))
            #vv[i][0]=vv[i][0]-tx
                #print(str(vv[i][0])+" "+str(vv[i][1])+" "+str(vv[i][2]))
            #vv[i][1]=ty+tempvv[i][1]
            #vv[i][1]=float(sy*vv[i][1])
            #vv[i][1]=vv[i][1]-ty
            #vv[i][2]=tz+tempvv[i][2]
            #vv[i][2]=float(sz*vv[i][2])
            #vv[i][2]=vv[i][2]-tz
            tempvv[i]=copy.deepcopy(vv[i])
                
        self.master.vert=copy.deepcopy(tempvv)
        '''self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,self.master.pannel_02.vrp,self.master.pannel_02.vpn,self.master.pannel_02.vup,self.master.pannel_02.prp,tempvv,
                                          self.master.pannel_02.faces,self.master.pannel_02.window,self.master.pannel_02.view)'''
        
        self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,self.master.camera.camcount,self.master.camera.name,self.master.camera.proj,self.master.camera.vrp,self.master.camera.vpn
            ,self.master.camera.vup,self.master.camera.prp,tempvv,
                                          self.master.pannel_02.faces,self.master.camera.window,self.master.camera.view)
        #self.master.ob_canvas_frame.canvas.after(50)        #set 50ms delay
######################################################################################################################################

######################################################################################################################################
class cl_pannel_06():
    def __init__(self, master):
        #print("CP6")
        self.master=master
        camlist=self.master.camera.name
        self.f = Frame(self.master.ob_root_window) 
        self.innerf = Frame(self.f)
        col=1
        
        self.dlabelText1=StringVar()
        self.dlabelText1.set("Select Camera:")
        self.dlabelDir1=Label(self.innerf, textvariable=self.dlabelText1)
        self.dlabelDir1.grid(row=1, column=col)
        col+=1  
        
        self.dvar1 = StringVar()
        self.drop = OptionMenu(self.innerf,self.dvar1,*camlist)
        self.drop.grid(row=1, column=col)
        col+=1  

        self.labelText1=StringVar()
        self.labelText1.set("VRP 1([x,y,z]):")
        self.labelDir1=Label(self.innerf, textvariable=self.labelText1)
        self.labelDir1.grid(row=1, column=col)
        col+=1  
        
        self.avar1 = StringVar()
        self.avar2 = StringVar()
        self.avar3 = StringVar()
        self.avar1.set("0")
        self.avar2.set("0")
        self.avar3.set("0")
        self.sx1=Entry(self.innerf,width=3, textvariable=self.avar1)
        self.sx1.grid(row=1, column=col)
        col+=1
        self.sy1=Entry(self.innerf,width=3, textvariable=self.avar2)
        self.sy1.grid(row=1, column=col)
        col+=1
        self.sz1=Entry(self.innerf,width=3, textvariable=self.avar3)
        self.sz1.grid(row=1, column=col)
        col+=1
        
        self.labelText2=StringVar()
        self.labelText2.set("VRP 2([x,y,z]):")
        self.labelDir2=Label(self.innerf, textvariable=self.labelText2)
        self.labelDir2.grid(row=1, column=col)
        col+=1  
        
        self.bvar1 = StringVar()
        self.bvar2 = StringVar()
        self.bvar3 = StringVar()
        self.bvar1.set("1")
        self.bvar2.set("1")
        self.bvar3.set("1")
        self.sx2=Entry(self.innerf,width=3, textvariable=self.bvar1)
        self.sx2.grid(row=1, column=col)
        col+=1
        self.sy2=Entry(self.innerf,width=3, textvariable=self.bvar2)
        self.sy2.grid(row=1, column=col)
        col+=1
        self.sz2=Entry(self.innerf,width=3, textvariable=self.bvar3)
        self.sz2.grid(row=1, column=col)
        col+=1
        
        self.labelText3=StringVar()
        self.labelText3.set("Steps:")
        self.labelDir3=Label(self.innerf, textvariable=self.labelText3)
        self.labelDir3.grid(row=1, column=col)
        col+=1
        self.w1 = Spinbox(self.innerf, from_=0, to=10, width=3)
        self.w1.grid(row=1, column=col)
        col+=1
        
        self.scalebut = Button(self.innerf, text="Fly", fg="blue", command=self.fly_callback)
        self.scalebut.grid(row=1, column=col)
        col+=1
        
        self.innerf.pack(side="left")
        self.f.pack()
        
    def fly_callback(self):        
        #print(self.v.get())
        #print("scale")
        
        #print(self.master.pannel_02.vrp[0])
        #print(self.master.pannel_02.vrp[1])
        #print(self.master.pannel_02.vrp[2])
        selcam=self.dvar1.get()
        #print(selcam)
        xi=0
        #print(self.master.camera.vrp)
        for i in range(len(self.master.camera.name)):
            #print(self.master.camera.name[i]) 
            if(selcam==self.master.camera.name[i]):
                xi=i
                break
            
        vrpx=float(self.bvar1.get())
        vrpy=float(self.bvar2.get())
        vrpz=float(self.bvar3.get())
        
        
        '''self.master.pannel_02.vrp[0]=vrpx
        self.master.pannel_02.vrp[1]=vrpy
        self.master.pannel_02.vrp[2]=vrpz'''
        
        self.master.camera.vrp[xi][0]=vrpx
        self.master.camera.vrp[xi][1]=vrpy
        self.master.camera.vrp[xi][2]=vrpz
        
        '''self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,
                                          self.master.pannel_02.vrp,self.master.pannel_02.vpn,self.master.pannel_02.vup,self.master.pannel_02.prp,self.master.vert,
                                          self.master.pannel_02.faces,self.master.pannel_02.window,self.master.pannel_02.view)'''
        
        self.master.ob_world.draw_figures(self.master.ob_canvas_frame.canvas,self.master.pannel_02.faceslen,1,self.master.camera.camcount,self.master.camera.name,self.master.camera.proj,self.master.camera.vrp,self.master.camera.vpn
            ,self.master.camera.vup,self.master.camera.prp,self.master.vert,
                                          self.master.pannel_02.faces,self.master.camera.window,self.master.camera.view)
        #self.master.ob_canvas_frame.canvas.after(50)        #set 50ms delay
######################################################################################################################################
            
######################################################################################################################################
'''class cl_pannel_01:
    
    def __init__(self, master):
        self.var_filename = StringVar()
        self.var_filename.set('')
        self.filename=""
        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
        #self.button = Button(frame, text="Hello", fg="red", command=self.say_hi)
        #self.button.pack(side=LEFT)
        #self.hi_there = Button(frame, text="Ask for a string", command=self.ask_for_string)
        #self.hi_there.pack(side=LEFT)  
        #self.hi_there = Button(frame, text="Ask for a float", command=self.ask_for_string)
        #self.hi_there.pack(side=LEFT)
        self.file_dialog_button = Button(frame, text="Open File Dialog", fg="blue", command=self.browse_file)
        self.file_dialog_button.pack(side=LEFT)        

    def say_hi(self):
        print ( "hi there, everyone!")
        
    def ask_for_string(self):
        s=simpledialog.askstring('My Dialog', 'Please enter a string')
        print (s)
        
    def ask_for_float(self):
        f=simpledialog.askfloat('My Dialog', 'Please enter a string')
        print (f)
        
    def browse_file(self):
        self.var_filename.set(filedialog.askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.txt")]))
        self.filename= self.var_filename.get()
        print(self.filename)

class MyDialog(simpledialog.Dialog):
    
    def body(self, master):
        Label(master, text="Integer:").grid(row=0, sticky=W)
        Label(master, text="Float:").grid(row=1, column=0 ,sticky=W)
        Label(master, text="String:").grid(row=1, column=2 , sticky=W)
        self.e1 = Entry(master)
        self.e1.insert(0, 0)
        self.e2 = Entry(master)
        self.e2.insert(0, 4.2)
        self.e3 = Entry(master)
        self.e3.insert(0, 'Default text')
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=1, column=3)
        self.cb = Checkbutton(master, text="Hardcopy")
        self.cb.grid(row=3, columnspan=2, sticky=W)

    def apply(self):
        try:
            first = int(self.e1.get())
            second = float(self.e2.get())
            third=self.e3.get()
            self.result = first, second, third
        except ValueError:
            tkMessageBox.showwarning("Bad input", "Illegal values, please try again")
            
class StatusBar:

    def __init__(self, master):
        self.master=master
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()       

class cl_statusBar_frame:

    def __init__(self, master):
        self.master=master
        status = StatusBar(master.ob_root_window)
        status.pack(side=BOTTOM, fill=X)
        status.set('%s','This is the status bar')

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
		
class cl_menu:
    
    def __init__(self, master):
        self.master=master
        self.menu = Menu(master.ob_root_window)
        master.ob_root_window.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.menu_callback)
        self.filemenu.add_command(label="Open...", command=self.menu_callback)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.menu_callback)
        self.dummymenu = Menu(self.menu)
        self.menu.add_cascade(label="Dummy", menu=self.dummymenu)
        self.dummymenu.add_command(label="Item1", command=self.menu_item1_callback)
        self.dummymenu.add_command(label="Item2", command=self.menu_item2_callback)   
        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.menu_help_callback)        

    def menu_callback(self):
        print ("called the menu callback!")
                        
    def menu_help_callback(self):
        print ("called the help menu callback!") 
        
    def menu_item1_callback(self):
        print ("called item1 callback!")    

    def menu_item2_callback(self):
        print ("called item2 callback!") 
		
class cl_toolbar:
    
    def __init__(self, master):
        self.master=master
        self.toolbar = Frame(master.ob_root_window)
        self.button = Button(self.toolbar, text="Draw", width=16, command=self.toolbar_draw_callback)
        self.button.pack(side=LEFT, padx=2, pady=2)
        self.button = Button(self.toolbar, text="Toolbar Button 2", width=16, command=self.toolbar_callback)
        self.button.pack(side=RIGHT, padx=2, pady=2)
        self.toolbar.pack(side=TOP, fill=X)
		
    def toolbar_draw_callback(self):
        #self.master.ob_world.create_graphic_objects(self.master.ob_canvas_frame.canvas)
        #temp_canvas=self.master.ob_canvas_frame.canvas
        #line1=temp_canvas.create_line(0,0,temp_canvas.cget("width"),temp_canvas.cget("height"))
        #line2=temp_canvas.create_line(temp_canvas.cget("width"),0,0,temp_canvas.cget("height"))
        #oval=temp_canvas.create_oval(int(0.25*int(temp_canvas.cget("width"))),
            #int(0.25*int(temp_canvas.cget("height"))),
            #int(0.75*int(temp_canvas.cget("width"))),
            #int(0.75*int(temp_canvas.cget("height"))))
        print ( "called the draw callback!")
    
    def toolbar_callback(self):
        print ( "called the toolbar callback!")'''
###################################################################################################################################### 