# Deshmukh, Omkar
# 1001-275-806
# 2015-04-20
# Assignment_04

###################################################################################################################################### 
from numpy  import *
from math import *
from tkinter import *
from PIL import ImageTk, Image, ImageDraw

from numpy import linalg as LA
import numpy as NP

import copy

class cl_world:
    tempv=[[]]
    masterdrawv=[]
    masterindex=0
    
    def __init__(self, objects=[],canvases=[]):     #constructor of the graphics class to init
        #print("cl world")
        self.objects=objects
        self.canvases=canvases
        #self.display
        self.redv=[[]]
        
    def add_canvas(self,canvas):    #adds a new canvas to the canvases array
        self.canvases.append(canvas)
        canvas.world=self           #sets the current canvas world to the current object?
    
    def create_graphic_objects(self,canvas):   #draws objects on the canvas 
        self.objects.append(canvas.create_line(0,0,canvas.cget("width"),canvas.cget("height")))
        self.objects.append(canvas.create_line(canvas.cget("width"),0,0,canvas.cget("height")))
        self.objects.append(canvas.create_oval(int(0.25*int(canvas.cget("width"))),
            int(0.25*int(canvas.cget("height"))),
            int(0.75*int(canvas.cget("width"))),
            int(0.75*int(canvas.cget("height")))))
      
    def draw_camera_frames(self,canvas,name=[],view=[[]]):
        #print(name)
        for i in range(len(view)):
            #print(i)
            self.objects.append(canvas.create_rectangle(int(view[i][0]*int(canvas.cget("width"))),
                                                    int(view[i][1]*int(canvas.cget("height"))), int(view[i][2]*int(canvas.cget("width"))),
                                                    int(view[i][3]*int(canvas.cget("height"))),fill="white"))
            self.objects.append(canvas.create_text(int(view[i][0]*int(canvas.cget("width"))),int(view[i][1]*int(canvas.cget("height"))),text=name[len(view)-i-1]))
            
        #print(len(self.objects))
            
    def draw_figures(self,canvas,faceslen,steps,camcount,xname=[],xproj=[],xvrp=[[]],xvpn=[[]],xvup=[[]],xprp=[[]],v=[[]],f=[[]],xw=[[]],xs=[[]]):
        '''print(name)
        print(proj)
        print(vrp)
        print(vpn)
        print(vup)
        print(prp)
        print(w)
        print(s)
        print(camcount)'''
        canvas.delete("all")
        vertices=v
        f=f
        faceslen=faceslen
        
        for xi in range(camcount):
            name=xname[xi]
            vrp=xvrp[xi]
            vpn=xvpn[xi]
            vup=xvup[xi]
            prp=xprp[xi]
            w=xw[xi]
            s=xs[xi]
            window=w
            view=s
            
            midarray=[[float(vrp[0]),float(vpn[0]),float(vup[0]),float(prp[0])],
              [float(vrp[1]),float(vpn[1]),float(vup[1]),float(prp[1])],
              [float(vrp[2]),float(vpn[2]),float(vup[2]),float(prp[2])],
              [1,1,1,1]]

            t=[[1,0,0,-float(vrp[0])],
                [0,1,0,-float(vrp[1])],
                 [0,0,1,-float(vrp[2])],
                  [0,0,0,1]]
        
            inter=midarray
            inter[0][0]=t[0][0]*midarray[0][0]+t[0][1]*midarray[1][0]+t[0][2]*midarray[2][0]+t[0][3]*midarray[3][0]
            inter[1][0]=t[1][0]*midarray[0][0]+t[1][1]*midarray[1][0]+t[1][2]*midarray[2][0]+t[1][3]*midarray[3][0]
            inter[2][0]=t[2][0]*midarray[0][0]+t[2][1]*midarray[1][0]+t[2][2]*midarray[2][0]+t[2][3]*midarray[3][0]
            inter[3][0]=t[3][0]*midarray[0][0]+t[3][1]*midarray[1][0]+t[3][2]*midarray[2][0]+t[3][3]*midarray[3][0]

            ########11111111########        
            t=NP.matrix(t)
    
            temp1=0.0
            temp2=0.0
            
            if ((vpn[1]*vpn[1])+(vpn[2]*vpn[2])) == 0:
                temp1=1
            else:
                temp1=vpn[2]/math.sqrt((vpn[1]*vpn[1])+(vpn[2]*vpn[2]))
    
            if ((vpn[1]*vpn[1])+(vpn[2]*vpn[2])) == 0:
                temp2=0
            else:
                temp2=-(vpn[1])/math.sqrt((vpn[1]*vpn[1])+(vpn[2]*vpn[2]))
    
            rotx=[[1,0,0,0],
                  [0,temp1,temp2,0],
                  [0,-temp2,temp1,0],
                  [0,0,0,1]] 
    
            tempinter=copy.deepcopy(inter)
            tempinter=NP.matrix(tempinter)
            
            ########22222222########  
            rotx=NP.matrix(rotx)
        
            inter=rotx*tempinter
            inter=inter.tolist()
            inter[0][3]=tempinter.item(3)
            inter[1][3]=tempinter.item(7)
            inter[2][3]=tempinter.item(11)
            inter[3][3]=tempinter.item(15)
    
    
            temp1=inter[2][1]/math.sqrt((inter[0][1]*inter[0][1])+(inter[2][1]*inter[2][1]))
            temp2=-(inter[0][1])/math.sqrt((inter[0][1]*inter[0][1])+(inter[2][1]*inter[2][1]))
            roty=[[temp1,0,temp2,0],
                  [0,1,0,0],
                  [-temp2,0,temp1,0],
                  [0,0,0,1]]
         
            tempinter=copy.deepcopy(inter)
            inter=NP.matrix(inter)
         
            ########33333333########
            roty=NP.matrix(roty)
    
            inter=roty*inter
            inter=inter.tolist()
            tempinter=NP.matrix(tempinter)
            inter[0][3]=tempinter.item(3)
            inter[1][3]=tempinter.item(7)
            inter[2][3]=tempinter.item(11)
            inter[3][3]=tempinter.item(15)
    
    
            if ((inter[0][2]*inter[0][2])+(inter[1][2]*inter[1][2])) == 0:
                temp1=1
            else:
                temp1=inter[1][2]/math.sqrt((inter[0][2]*inter[0][2])+(inter[1][2]*inter[1][2]))
    
            if ((inter[0][2]*inter[0][2])+(inter[1][2]*inter[1][2])) == 0:
                temp2=0
            else:
                temp2=-(inter[0][2])/math.sqrt((inter[0][2]*inter[0][2])+(inter[1][2]*inter[1][2]))
        
            #temp1=inter[1][2]/math.sqrt((inter[0][2]*inter[0][2])+(inter[1][2]*inter[1][2]))
            #temp2=-(inter[0][2])/math.sqrt((inter[0][2]*inter[0][2])+(inter[1][2]*inter[1][2]))
            rotz=[[temp1,temp2,0,0],
                  [-temp2,temp1,0,0],
                  [0,0,1,0],
                  [0,0,0,1]]
              
            tempinter=copy.deepcopy(inter)
            inter=NP.matrix(inter)
    
            ########44444444########
            rotz=NP.matrix(rotz)
        
            inter=rotz*inter
            inter=inter.tolist()
            tempinter=NP.matrix(tempinter)
            inter[0][3]=tempinter.item(3)
            inter[1][3]=tempinter.item(7)
            inter[2][3]=tempinter.item(11)
            inter[3][3]=tempinter.item(15)
                
            if(xproj[xi]=="parallel"):
                #print("HAHA")
                #####################################Projection starts#####################################          
                
    
                temp1=(-(prp[0]-((window[1]+window[0])/2)))/prp[2]
                temp2=(-(prp[1]-((window[3]+window[2])/2)))/prp[2]
                shear=[[1,0,temp1,0],
                       [0,1,temp2,0],
                      [0,0,1,0],
                      [0,0,0,1]]
              
                tempinter=copy.deepcopy(inter)
                inter=NP.matrix(inter)
        
                ########55555555########
                shear=NP.matrix(shear)
        
                inter=shear*inter
                inter=inter.tolist()
                tempinter=NP.matrix(tempinter)
                inter[0][1]=tempinter.item(1)
                inter[0][2]=tempinter.item(2)
                inter[1][1]=tempinter.item(5)
                inter[1][2]=tempinter.item(6)
                inter[2][1]=tempinter.item(9)
                inter[2][2]=tempinter.item(10)
                inter[3][1]=tempinter.item(13)
                inter[3][2]=tempinter.item(14)
        
                if(window[5]>window[4]):
                    temp1=-window[4]
                else:
                    temp1=-window[5]
                tcw=[[1,0,0,-float((window[0]+window[1])/2)],
                      [0,1,0,-float((window[2]+window[3])/2)],
                       [0,0,1,temp1],
                     [0,0,0,1]]
        
                tempinter=copy.deepcopy(inter)
                inter=NP.matrix(inter)
        
                ########66666666########
                tcw=NP.matrix(tcw)
        
                inter=tcw*inter
                inter=inter.tolist()
                tempinter=NP.matrix(tempinter)
                inter[0][1]=tempinter.item(1)
                inter[0][2]=tempinter.item(2)
                inter[1][1]=tempinter.item(5)
                inter[1][2]=tempinter.item(6)
                inter[2][1]=tempinter.item(9)
                inter[2][2]=tempinter.item(10)
                inter[3][1]=tempinter.item(13)
                inter[3][2]=tempinter.item(14)
        
                temp3=0
                if (window[1]>window[0]):
                    temp1=4/(window[1]-window[0])
                else:
                    temp1=2/(window[0]-window[1])
        
                if (window[3]>window[2]):
                    temp2=4/(window[3]-window[2])
                else:
                    temp2=2/(window[2]-window[3])
        
                if (window[5]>window[4]):
                    temp3=1/(window[5]-window[4])
                else:
                    temp3=1/(window[4]-window[5])
            
                scale=[[temp1,0,0,0],
                       [0,temp2,0,0],
                     [0,0,temp3,0],
                     [0,0,0,1]]
                     #print(temp1)
                     #print(temp2)
                     #print(temp3)
                     ########77777777########
                scale=NP.matrix(scale)
        
            if(xproj[xi]=="perspective"):
                #print("HAHA")
               
                tcw=[[1,0,0,-float(inter[0][3])],
                      [0,1,0,-float(inter[1][3])],
                       [0,0,1,-float(inter[2][3])],
                     [0,0,0,1]]
                     
                tempinter=copy.deepcopy(inter)
                inter=NP.matrix(inter)
                
                ########55555555########

                tcw=NP.matrix(tcw)
        
                inter=tcw*inter
                inter=inter.tolist()
                tempinter=NP.matrix(tempinter)
                inter[0][1]=tempinter.item(1)
                inter[0][2]=tempinter.item(2)
                inter[0][3]=tempinter.item(3)
                inter[1][1]=tempinter.item(5)
                inter[1][2]=tempinter.item(6)
                inter[1][3]=tempinter.item(7)
                inter[2][1]=tempinter.item(9)
                inter[2][2]=tempinter.item(10)
                inter[2][3]=tempinter.item(11)
                inter[3][1]=tempinter.item(13)
                inter[3][2]=tempinter.item(14)
                
                temp1=(-(prp[0]-((window[1]+window[0])/2)))/prp[2]
                temp2=(-(prp[1]-((window[3]+window[2])/2)))/prp[2]
                shear=[[1,0,temp1,0],
                       [0,1,temp2,0],
                      [0,0,1,0],
                      [0,0,0,1]]
              
                tempinter=copy.deepcopy(inter)
                inter=NP.matrix(inter)
        
                ########66666666########
                shear=NP.matrix(shear)
        
                inter=shear*inter
                inter=inter.tolist()
                tempinter=NP.matrix(tempinter)
                inter[0][1]=tempinter.item(1)
                inter[0][2]=tempinter.item(2)
                inter[1][1]=tempinter.item(5)
                inter[1][2]=tempinter.item(6)
                inter[2][1]=tempinter.item(9)
                inter[2][2]=tempinter.item(10)
                inter[3][1]=tempinter.item(13)
                inter[3][2]=tempinter.item(14)
                inter[0][3]=-inter[0][0]
                inter[1][3]=-inter[1][0]
                inter[2][3]=-inter[2][0]
                
                
                temp3=0
                if (math.fabs(inter[2][0]+window[5])>math.fabs(inter[2][0]+window[4])):
                    temp1=(math.fabs(inter[2][0]))/(((window[1]-window[0])/2)*(inter[2][0]+window[5]))
                else:
                    temp1=(math.fabs(inter[2][0]))/(((window[1]-window[0])/2)*(inter[2][0]+window[4]))
        
                if (math.fabs(inter[2][0]+window[5])>math.fabs(inter[2][0]+window[4])):
                    temp1=(math.fabs(inter[2][0]))/(((window[3]-window[2])/2)*(inter[2][0]+window[5]))
                else:
                    temp1=(math.fabs(inter[2][0]))/(((window[3]-window[2])/2)*(inter[2][0]+window[4]))
        
                if (math.fabs(inter[2][0]+window[5])>math.fabs(inter[2][0]+window[4])):
                    temp3=1/(inter[2][0]+window[5])
                else:
                    temp3=1/(inter[2][0]+window[4])
            
                scale=[[temp1,0,0,0],
                       [0,temp2,0,0],
                     [0,0,temp3,0],
                     [0,0,0,1]]
                     #print(temp1)
                     #print(temp2)
                     #print(temp3)
                     ########77777777########
                scale=NP.matrix(scale)
                
             
            inpv=[vertices[0][0],vertices[0][1],vertices[0][2],1]
            #print(t)
        
            intervert=[[]]
            iv=0
            #print("***********")
            for i in range(len(vertices)):
                inpv=[vertices[i][0],vertices[i][1],vertices[i][2],1]
                inpv=NP.matrix(inpv)
                #print(" ")
                #print(inpv)
                tempvv=t*inpv.T             #1 
            
                #print(tempvv.T)
                tempvv=rotx*tempvv          #2
                #print(tempvv.T)
                tempvv=roty*tempvv          #3
                #print(tempvv.T)
                tempvv=rotz*tempvv          #4
                #print(rotz)
                #print(tempvv.T)
                #print(tempvv.T[0][0][0])
                if(xproj[xi]=="parallel"):
                
                #print(tempvv.T)
                
                    tempvv=shear*tempvv         #5
                    tempvv=tcw*tempvv           #6
                #print(tempvv.T)
                #tempvv=scale*tempvv         #7#i dont know why 'not scaling' gives the output matching to profs output
                                        # if i use scaling it gives a smaller output in size as compared to prof's
                #print(tempvv.T)
                    tempvv=tempvv.T
                
                if(xproj[xi]=="perspective"):
                    
                    #print(tempvv.T)
                    tempvv=tcw*tempvv           #6
                    #print(tempvv.T)
                    tempvv=shear*tempvv         #5
                    #print(tempvv.T)
                    #tempvv=scale*tempvv         #7#i dont know why 'not scaling' gives the output matching to profs output
                                            # if i use scaling it gives a smaller output in size as compared to prof's
                    #print(tempvv.T)
                    #print(tempvv.T)
                    #print(scale)
                    tempvv=tempvv.T   
                #tempvv=tempvv.tolist()
                #print(tempvv)
                #print("llalala")
                #print(self.vertices[i])
                #print(tempvv.item(0))
        
                intervert[iv]=[tempvv.item(0),tempvv.item(1),tempvv.item(2)]
                #intervert=intervert[iv].tolist()
                intervert.append([])
                iv+=1
                #print(intervert[iv-1][0:3])
                #print("bahshha")
        
            intervert.pop()

            #print("OG")
            #print(self.vertices)
            #print("inter")
            #print(intervert)
            #print("master")
            #print(self.master.vert)
            #self.master.vert=copy.deepcopy(intervert)
            #print("copy master")
            #print(self.master.vert)

        #####################################Projection ends#####################################
        
        #####################################  Clipping Starts here  #####################################
                #indent wrt to this point
            '''xmin=window[0]
            xmax=window[1]
            ymin=window[2]
            ymax=window[3]
            zmin=window[4]
            zmax=window[5]'''
        
            '''xmin=0
            xmax=1
            ymin=0
            ymax=1
            zmin=0
            zmax=1
        
            def compoutcode(inpx1,inpy1,inpz1):
                oc=[0,0,0,0,0,0,0]        #t,b,l,r,n,f,all
                #oc2=[0,0,0,0,0,0,0]        #t,b,l,r,n,f,all
                if (inpy1>ymax):
                    oc[0]=1
                    oc[6]+=oc[0]
                elif (inpy1<ymin):
                    oc[1]=1
                    oc[6]+=oc[1]
                
                if (inpx1>xmax):
                    oc[3]=1
                    oc[6]+=oc[3]
                elif (inpx1<xmin):
                    oc[2]=1
                    oc[6]+=oc[2]
            
                if (inpz1>zmax):
                    oc[5]=1
                    oc[6]+=oc[5]
                elif (inpz1<zmin):
                    oc[4]=1
                    oc[6]+=oc[4]
                return oc
        
            def lineclip(x0,y0,z0,x1,y1,z1):   
                accept=False
                done=False
                oc0=compoutcode(x0,y0,z0)
                oc1=compoutcode(x1,y1,z1)
                ocout=[]
                tempx=0
                tempy=0
                tempz=0
            
                while(True):
                    if(oc0[6]==0 and oc1[6]==0):
                        accept=True
                        done=True
                    elif(oc0[6] & oc1[6]!=0):
                        done=True
                    else:
                        if(oc0[6]!=0):
                            ocout=oc0
                        else:
                            ocout=oc1
                        
                        if(ocout[0]==1):
                            tempx=x0+(x1-x0)*((ymax-y0)/(y1-y0))
                            tempy=ymax
                            tempz=z0+(z1-z0)*((ymax-y0)/(y1-y0))
                        elif(ocout[1]==1):
                            tempx=x0+(x1-x0)*((ymin-y0)/(y1-y0))
                            tempy=ymin
                            tempz=z0+(z1-z0)*((ymin-y0)/(y1-y0))
                        elif(ocout[3]==1):
                            tempx=xmax
                            tempy=y0+(y1-y0)*((xmax-x0)/(x1-x0))
                            tempz=z0+(z1-z0)*((xmax-x0)/(x1-x0))
                        elif(ocout[2]==1):
                            tempx=xmin
                            tempy=y0+(y1-y0)*((xmin-x0)/(x1-x0))
                            tempz=z0+(z1-z0)*((xmin-x0)/(x1-x0))
                        elif(ocout[4]==1):
                            tempz=zmin
                        elif(ocout[5]==1):
                            tempz=zmax
                        
                        if(ocout[6]==oc0[6]):
                            x0=tempx
                            y0=tempy
                            z0=tempz
                            oc0=compoutcode(x0,y0,z0)
                        else:
                            x1=tempx
                            y1=tempy
                            z1=tempz
                            oc1=compoutcode(x1,y1,z1)
                        if(done==True):
                            break
                
            return x0,y0,z0,x1,y1,z1,accept'''
         
            '''def newclip(ax,ay,az,bx,by,bz):
                lx=bx-ax
                rx=ax
                ly=by-ay
                ry=ay
                lz=bz-az
                rz=az
                accept=False
            
                coeff=[ [1,0,0,-1],
                       [1,0,0,0],
                        [0,1,0,-1],
                        [0,1,0,0],
                        [0,0,1,-1],
                        [0,0,1,0]]
            
            
                rightt=99
                leftt=99
                topt=99
                bott=99
                backt=99
                frontt=99
            
                try:
                    rightt=-(coeff[0][0]*rx+coeff[0][1]*ry+coeff[0][2]*rz+coeff[0][3])/(coeff[0][0]*lx+coeff[0][1]*ly+coeff[0][2]*lz)
                except:
                    pass
                try:
                    leftt=-(coeff[1][0]*rx+coeff[1][1]*ry+coeff[1][2]*rz+coeff[1][3])/(coeff[1][0]*lx+coeff[1][1]*ly+coeff[1][2]*lz)
                except:
                    pass
                try:
                    topt=-(coeff[2][0]*rx+coeff[2][1]*ry+coeff[2][2]*rz+coeff[2][3])/(coeff[2][0]*lx+coeff[2][1]*ly+coeff[2][2]*lz)
                except:
                    pass
                try:
                    bott=-(coeff[3][0]*rx+coeff[3][1]*ry+coeff[3][2]*rz+coeff[3][3])/(coeff[3][0]*lx+coeff[3][1]*ly+coeff[3][2]*lz)
                except:
                    pass
                try:
                    backt=-(coeff[4][0]*rx+coeff[4][1]*ry+coeff[4][2]*rz+coeff[4][3])/(coeff[4][0]*lx+coeff[4][1]*ly+coeff[4][2]*lz)
                except:
                    pass
                try:
                    frontt=-(coeff[5][0]*rx+coeff[5][1]*ry+coeff[5][2]*rz+coeff[5][3])/(coeff[5][0]*lx+coeff[5][1]*ly+coeff[5][2]*lz)
                except:
                    pass
            
                rightx=lx*rightt+rx
                leftx=lx*leftt+rx
                topx=lx*topt+rx
                botx=lx*bott+rx
                backx=lx*backt+rx
                frontx=lx*frontt+rx
                
                righty=ly*rightt+ry
                lefty=ly*leftt+ry
                topy=ly*topt+ry
                boty=ly*bott+ry
                backy=ly*backt+ry
                fronty=ly*frontt+ry
            
                rightz=lz*rightt+rz
                leftz=lz*leftt+rz
                topz=lz*topt+rz
                botz=lz*bott+rz
                backz=lz*backt+rz
                frontz=lz*frontt+rz
            
                if(rightt>=0 and rightt<=1 and rightx>=0 and rightx<=1 and righty>=0 and righty<=1 and rightz>=0 and rightz<=1):
                    rightop=1
                else:
                    rightop=0
                if(leftt>=0 and leftt<=1 and leftx>=0 and leftx<=1 and lefty>=0 and lefty<=1 and leftz>=0 and leftz<=1):
                    leftop=1
                else:
                    leftop=0
                if(topt>=0 and topt<=1 and topx>=0 and topx<=1 and topy>=0 and topy<=1 and topz>=0 and topz<=1):
                    topop=1
                else:
                    topop=0
                if(bott>=0 and bott<=1 and botx>=0 and botx<=1 and boty>=0 and boty<=1 and botz>=0 and botz<=1):
                    botop=1
                else:
                    botop=0
                if(backt>=0 and backt<=1 and backx>=0 and backx<=1 and backy>=0 and backy<=1 and backz>=0 and backz<=1):
                    backop=1
                else:
                    backop=0
                if(frontt>=0 and frontt<=1 and frontx>=0 and frontx<=1 and fronty>=0 and fronty<=1 and frontz>=0 and frontz<=1):
                    frontop=1
                else:
                    frontop=0
            
                if(rightop==1):
                    ax=rightx
                    ay=righty
                    az=rightz
                    rightop=0
                    accept=True
                elif(leftop==1):
                    ax=leftx
                    ay=lefty
                    az=leftz
                    leftop=0
                    accept=True
                elif(topop==1):
                    ax=topx
                    ay=topy
                    az=topz
                    topop=0
                    accept=True
                elif(botop==1):
                    ax=botx
                    ay=boty
                    az=botz
                    botop=0
                    accept=True
                elif(backop==1):
                    ax=backx
                    ay=backy
                    az=backz
                    backop=0
                    accept=True
                
                if(leftop==1):
                    bx=leftx
                    by=lefty
                    bz=leftz
                    leftop=0
                    accept=True
                elif(topop==1):
                    bx=topx
                    by=topy
                    bz=topz
                    topop=0
                    accept=True
                elif(botop==1):
                    bx=botx
                    by=boty
                    bz=botz
                    botop=0
                    accept=True
                elif(backop==1):
                    bx=backx
                    by=backy
                    bz=backz
                    backop=0    
                    accept=True
                elif(frontop==1):
                    bx=frontx
                    by=backy
                    bz=backz
                    backop=0   
                    accept=True
                
                return ax,ay,az,bx,by,bz,accept     
                
        
            #ax,ay,az,bx,by,bz=newclip(2,7.3,-0.5,-2,-6.7,1.5)
            #print(ax,ay,az,bx,by,bz)       
            #print(intervert)
            clipv=copy.deepcopy(intervert)
            clipresult=[[]]
            cri=0
                if faceslen==3:                              
                    for i in range(len(f)):
                        ox0=clipv[int(f[i][0]-1)][0] 
                        oy0=clipv[int(f[i][0]-1)][1]
                        oz0=clipv[int(f[i][0]-1)][2]
                        ox1=clipv[int(f[i][1]-1)][0] 
                        oy1=clipv[int(f[i][1]-1)][1]
                        oz1=clipv[int(f[i][1]-1)][2]
                        #print("FFSF")
                        #print(ox0,oy0,oz0,ox1,oy1,oz1)
                        rx0,ry0,rz0,rx1,ry1,rz1,raccept=newclip(ox0,oy0,oz0,ox1,oy1,oz1)   
                        #print(rx0,ry0,rz0,rx1,ry1,rz1) 
                        if(raccept==True):
                        clipresult[cri]=[rx0,ry0,rz0,rx1,ry1,rz1]
                        clipresult.append([])
                        cri+=1
                    
                    ox0=clipv[int(f[i][1]-1)][0] 
                    oy0=clipv[int(f[i][1]-1)][1]
                    oz0=clipv[int(f[i][1]-1)][2]
                    ox1=clipv[int(f[i][2]-1)][0] 
                    oy1=clipv[int(f[i][2]-1)][1]
                    oz1=clipv[int(f[i][2]-1)][2]
                
                    #print(ox0,oy0,oz0,ox1,oy1,oz1)
                    rx0,ry0,rz0,rx1,ry1,rz1,raccept=newclip(ox0,oy0,oz0,ox1,oy1,oz1)   
                    #print(rx0,ry0,rz0,rx1,ry1,rz1) 
                    
                    if(raccept==True):
                        clipresult[cri]=[rx0,ry0,rz0,rx1,ry1,rz1]
                        clipresult.append([])
                        cri+=1
                    
                    ox0=clipv[int(f[i][2]-1)][0] 
                    oy0=clipv[int(f[i][2]-1)][1]
                    oz0=clipv[int(f[i][2]-1)][2]
                    ox1=clipv[int(f[i][0]-1)][0] 
                    oy1=clipv[int(f[i][0]-1)][1]
                    oz1=clipv[int(f[i][0]-1)][2]
                
                    #print(ox0,oy0,oz0,ox1,oy1,oz1)
                    rx0,ry0,rz0,rx1,ry1,rz1,raccept=newclip(ox0,oy0,oz0,ox1,oy1,oz1)   
                    #print(rx0,ry0,rz0,rx1,ry1,rz1) 
                    #print(rx0)
                    if(raccept==True):
                        clipresult[cri]=[rx0,ry0,rz0,rx1,ry1,rz1]
                        clipresult.append([])
                        cri+=1
                    
                clipresult.pop()
                #print(clipresult) 
                #print(clipresult)                                  
                drawv=[]
                for i in clipresult:
                    drawv.append(i[0:3])
                    drawv.append(i[3:])
                    
            
            
                for i in drawv:
                    print(i)
                
                #####################################  Clipping Ends here  #####################################'''
           
            #print(view)
            for i in range(steps):
                #canvas.delete("all")
                #for i in range(len(view)):
                self.objects.append(canvas.create_rectangle(int(view[0]*int(canvas.cget("width"))),
                                            int(view[1]*int(canvas.cget("height"))), int(view[2]*int(canvas.cget("width"))),
                                            int(view[3]*int(canvas.cget("height"))),fill="white"))
                self.objects.append(canvas.create_text(int(view[0]*int(canvas.cget("width"))),int(view[1]*int(canvas.cget("height"))),text=name,anchor=NW))
        
                #view=s
                drawv=copy.deepcopy(intervert)
        
                self.masterdrawv.append(drawv)
                
    
                ogviewxmin=view[0]*int(canvas.cget("width"))
                ogviewxmax=view[2]*int(canvas.cget("width"))
                ogviewymin=view[1]*int(canvas.cget("height"))
                ogviewymax=view[3]*int(canvas.cget("height"))
        
    
                for i in range(len(drawv)):
                    #for translating to -Wxmin,-Wymin
        
        
                    drawv[i][0]=drawv[i][0]-w[0]
                    drawv[i][1]=w[3]-drawv[i][1]          
    
                    #for scaling
                    sx=(float(ogviewxmax)-float(ogviewxmin))/(float(w[1])-float(w[0]))
                    sy=(float(ogviewymax)-float(ogviewymin))/(float(w[3])-float(w[2]))
            

                    #print(int(canvas.cget("width")))
                    #print(int(canvas.cget("height")))
        
                    drawv[i][0]=drawv[i][0]*sx
                    drawv[i][1]=drawv[i][1]*sy
        
    
                    #for translating to Vxmin,Vymin
                    drawv[i][0]=drawv[i][0]+ogviewxmin
                    drawv[i][1]=drawv[i][1]+ogviewymin
            
                    #print("ashd")
                    #print(drawv[i][0])
                    #print(drawv[i][1])
               
    
       
        
                if faceslen==3:                              
                    #draw the polygons(triangles using lines)
                    for i in range(len(f)):
                        self.objects.append(canvas.create_line(drawv[int(f[i][0]-1)][0], 
                                                   drawv[int(f[i][0]-1)][1],
                                                   drawv[int(f[i][1]-1)][0], 
                                                   drawv[int(f[i][1]-1)][1]))
                                                  
                        self.objects.append(canvas.create_line(drawv[int(f[i][1]-1)][0], 
                                                   drawv[int(f[i][1]-1)][1],
                                                   drawv[int(f[i][2]-1)][0], 
                                                   drawv[int(f[i][2]-1)][1]))
                                                  
                        self.objects.append(canvas.create_line(drawv[int(f[i][2]-1)][0], 
                                                   drawv[int(f[i][2]-1)][1],
                                                   drawv[int(f[i][0]-1)][0], 
                                                   drawv[int(f[i][0]-1)][1]))
                                                  
                if faceslen==4:                
                    #draw the polygons(quadrilaterals using lines)
                    for i in range(len(f)):
                        self.objects.append(canvas.create_line(drawv[int(f[i][0]-1)][0], 
                                                   drawv[int(f[i][0]-1)][1],
                                                   drawv[int(f[i][1]-1)][0], 
                                                   drawv[int(f[i][1]-1)][1]))
                                                  
                        self.objects.append(canvas.create_line(drawv[int(f[i][1]-1)][0], 
                                                   drawv[int(f[i][1]-1)][1],
                                                   drawv[int(f[i][2]-1)][0], 
                                                   drawv[int(f[i][2]-1)][1]))
                                                  
                        self.objects.append(canvas.create_line(drawv[int(f[i][2]-1)][0], 
                                                   drawv[int(f[i][2]-1)][1],
                                                   drawv[int(f[i][3]-1)][0], 
                                                   drawv[int(f[i][3]-1)][1]))
                    
                        self.objects.append(canvas.create_line(drawv[int(f[i][3]-1)][0], 
                                                   drawv[int(f[i][3]-1)][1],
                                                   drawv[int(f[i][0]-1)][0], 
                                                   drawv[int(f[i][0]-1)][1]))
                
            #self.redv=copy.deepcopy(intervert)
            #return intervert   
                           
            #print(drawv)
            #print("------------------------------")
            #self.masterdrawv.append(drawv)
            
        #print("------------------------------")
        #print("------------------------------")
        #print(self.masterdrawv)
        #print(len(self.objects))
######################################################################################################################################    
    #used to redraw the objects on the canvas in case of an event
    def redisplay(self,canvas,event,faceslen,camcount,v=[[]],f=[[]],xw=[[]],xs=[[]]):
        #index=self.masterindex
        index=0
        #print("len")
        #print(len(self.objects))
        #print((len(f)*faceslen))
        #print(       int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )        )
        faceslen=faceslen
        
            
        #print(len(view))
        #print(view[0][0])
        #print(self.objects)
        
            
        for xi in range(camcount):
            
            w=xw[xi]
            s=xs[xi]
            #window=w
            view=s
            
            try:
                
                #print(self.masterdrawv[xi])
                #print(xi)
                '''print("tryyyyyy d")
                for i in range(len(view)):'''
                #print(int((len(self.objects)-((len(f)*faceslen)+1))+index))
                #print(int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  ))
                canvas.coords(self.objects[ int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                           int(view[0]*int(event.width)),
                      int(view[1]*int(event.height)),
                      int(view[2]*int(event.width)),
                      int(view[3]*int(event.height)))
                index+=1
                
                #print(int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  ))
                canvas.coords(self.objects[ int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                           int(view[0]*int(event.width)),
                      int(view[1]*int(event.height)))
                index+=1
                
                #print("hahah d")
                    
                    
                ogviewxmin=view[0]*int(event.width)
                ogviewxmax=view[2]*int(event.width)
                ogviewymin=view[1]*int(event.height)
                ogviewymax=view[3]*int(event.height)
                
                #print("sad")
                self.redv=copy.deepcopy(self.masterdrawv[xi])
                #print((self.redv))
                #print("HUH")
                #print(w)
                for i in range(len(self.redv)):
                    #for translating to -Wxmin,-Wymin
                
                    
                    self.redv[i][0]=self.redv[i][0]-w[0]
                    self.redv[i][1]=w[3]-self.redv[i][1]          
            
                    
                    #print(w)
                    #for scaling
                    sx=(float(ogviewxmax)-float(ogviewxmin))/(float(w[1])-float(w[0]))
                    sy=(float(ogviewymax)-float(ogviewymin))/(float(w[3])-float(w[2]))
                    #print(sx)
                    #print(sy)
                    
                    #print(int(canvas.cget("width")))
                    #print(int(canvas.cget("height")))
                
                    self.redv[i][0]=self.redv[i][0]*sx
                    self.redv[i][1]=self.redv[i][1]*sy
                
                    
                    #for translating to Vxmin,Vymin
                    self.redv[i][0]=self.redv[i][0]+ogviewxmin
                    self.redv[i][1]=self.redv[i][1]+ogviewymin
                    
                #print("WEWWWWWWW")
                    
            except:
                #print("WTFFFFFFFFFFFFFFF")
                pass
            
            #print(index)
            if self.objects:                                                      
                if faceslen==3: 
                    
                
                    for i in range(len(f)):
                        canvas.coords(self.objects[int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                        self.redv[int(f[i][0]-1)][0], 
                                        self.redv[int(f[i][0]-1)][1],
                                        self.redv[int(f[i][1]-1)][0], 
                                        self.redv[int(f[i][1]-1)][1])
                        index+=1
                        canvas.coords(self.objects[int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                        self.redv[int(f[i][1]-1)][0], 
                                        self.redv[int(f[i][1]-1)][1],
                                        self.redv[int(f[i][2]-1)][0], 
                                        self.redv[int(f[i][2]-1)][1])
                        index+=1
                        canvas.coords(self.objects[ int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                        self.redv[int(f[i][2]-1)][0], 
                                        self.redv[int(f[i][2]-1)][1],
                                        self.redv[int(f[i][0]-1)][0], 
                                        self.redv[int(f[i][0]-1)][1])
                        index+=1             
                        
                if faceslen==4:
                    
                    #index+=1
                    
                    for i in range(len(f)):
                        canvas.coords(self.objects[ int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                        self.redv[int(f[i][0]-1)][0], 
                                        self.redv[int(f[i][0]-1)][1],
                                        self.redv[int(f[i][1]-1)][0], 
                                        self.redv[int(f[i][1]-1)][1])
                        index+=1
                        canvas.coords(self.objects[int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                        self.redv[int(f[i][1]-1)][0], 
                                        self.redv[int(f[i][1]-1)][1],
                                        self.redv[int(f[i][2]-1)][0], 
                                        self.redv[int(f[i][2]-1)][1])
                        index+=1
                        canvas.coords(self.objects[ int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                        self.redv[int(f[i][2]-1)][0], 
                                        self.redv[int(f[i][2]-1)][1],
                                        self.redv[int(f[i][3]-1)][0], 
                                        self.redv[int(f[i][3]-1)][1])
                        index+=1
                        canvas.coords(self.objects[ int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  )],
                                        self.redv[int(f[i][3]-1)][0], 
                                        self.redv[int(f[i][3]-1)][1],
                                        self.redv[int(f[i][0]-1)][0], 
                                        self.redv[int(f[i][0]-1)][1])
                        index+=1
            #print(int(    len(self.objects) - (  ((len(f)*faceslen)+2)*(camcount)+index    )  ))
        self.masterindex=index
###################################################################################################################################### 