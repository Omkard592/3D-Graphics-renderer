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

class cl_camera:
    
    def __init__(self):
        self.camcount=0
        self.cc=0
        self.name=[[]]
        self.proj=[[]]
        self.vrp=[[]]
        self.vpn=[[]]
        self.vup=[[]]
        self.prp=[[]]
        self.window=[[]]
        self.view=[[]]
        '''ni=0
        pi=0
        vrpi=0
        vpni=0
        vupi=0
        prpi=0
        wi=0
        vi=0'''
        
        with open("cameras_04.txt") as inp:
            inplines = inp.read().splitlines()
    
        #print(inplines)
        #print(camdata)
        ni=-1
        pi=-1
        vrpi=-1
        vpni=-1
        vupi=-1
        prpi=-1
        wi=-1
        vi=-1  
        for line in inplines:
            #print("WUT")
            #line=line[0:len(line-1)]
            #print(line)
        
            if line[0]=='c':
                self.camcount+=1
                ni+=1
                pi+=1
                vrpi+=1
                vpni+=1
                vupi+=1
                prpi+=1
                wi+=1
                vi+=1
                
                self.name[ni]=" "
                self.proj[pi]="parallel"
                self.vrp[vrpi]=[0,0,0]
                self.vpn[vpni]=[0,0,1]
                self.vup[vupi]=[0,1,0]
                self.prp[prpi]=[0,0,1]
                self.window[wi]=[-1,1,-1,1,-1,1]
                self.view[vi]=[0.1,0.1,0.4,0.4]
                
                self.name.append([])
                self.proj.append([])
                self.vrp.append([])
                self.vpn.append([])
                self.vup.append([])
                self.prp.append([])
                self.window.append([])
                self.view.append([])
                
                
                
            if line[0]=='i':
                self.name[ni]=line[2:]
                #self.name.append([])
                #ni+=1
                
            if line[0]=='t':
                self.proj[pi]=line[2:]
                #self.proj.append([])
                #pi+=1
                
            if line[0]=='r':
                line=line[2:]
                self.vrp[vrpi]=[float(d) for d in line.split()]
                #self.vrp.append([])
                #vrpi+=1
                
            if line[0]=='n':
                line=line[2:]
                self.vpn[vpni]=[float(d) for d in line.split()]
                #self.vpn.append([])
                #vpni+=1
                
            if line[0]=='u':
                line=line[2:]
                self.vup[vupi]=[float(d) for d in line.split()]
                #self.vup.append([])
                #vupi+=1
                
            if line[0]=='p':
                line=line[2:]
                self.prp[prpi]=[float(d) for d in line.split()]
                #self.prp.append([])
                #prpi+=1
                
            if line[0]=='w':
                line=line[2:]
                self.window[wi]=[float(c) for c in line.split()]
                #self.window.append([])
                #wi+=1
                
            if line[0]=='s':
                line=line[2:]
                self.view[vi]=[float(d) for d in line.split()]
                #self.view.append([])
                #vi+=1
          
                
        '''print("HAHAHHAHAH")
        print(self.camcount)
        print(self.name)
        print(self.proj)
        print(self.vrp)
        print(self.vpn)
        print(self.vup)
        print(self.prp)
        print(self.window)
        print(self.view) '''       
        self.name.pop()
        self.proj.pop()
        self.vrp.pop()
        self.vpn.pop()
        self.vup.pop()
        self.prp.pop()
        self.window.pop()
        self.view.pop()
        '''print(self.camcount)
        print(self.name)
        print(self.proj)
        print(self.vrp)
        print(self.vpn)
        print(self.vup)
        print(self.prp)
        print(self.window)
        print(self.view)'''
        
        #print("cc")
        #print(self.camcount)
######################################################################################################################################