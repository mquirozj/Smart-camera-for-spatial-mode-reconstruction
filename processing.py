# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:03:29 2022

@author: mquir
"""
from numpy import * #package to numerical calculations
from matplotlib.pyplot import * #package to plot
import glob #read files from a directory with extension png
import cv2 #read images
from skimage.color import rgb2gray #from rgb to gray

def cropImage_v2(Im,high_s,high_i,width_left,width_right):
    r,c=shape(Im)
    I=Im[high_s:high_i,width_left:width_right]
    return I

def DownSampling_v2(FieldF,SquareSize):
    OutPixel,OutPixel2=shape(FieldF)
    res=OutPixel%SquareSize
    Limit=(OutPixel-res)/SquareSize
    
    res2=OutPixel2%SquareSize
    Limit2=(OutPixel2-res2)/SquareSize
    FieldD=zeros([int(Limit),int(Limit2)])
    
    for m in range(int(Limit)):
        for p in range(int(Limit2)):
            #print(m,p,Limit,Limit2)
            ini_m=SquareSize*(m)
            fin_m=SquareSize*(m+1)-1
            ini_n=SquareSize*(p)
            fin_n=SquareSize*(p+1)-1
            Im=FieldF[ini_m:fin_m,ini_n:fin_n]
            FieldD[m,p]=sum(sum(Im))/(SquareSize**2)
    return FieldD

def readimage(Nameimage,pixeldown):    
    I_rgb=cv2.imread(Nameimage, cv2.IMREAD_COLOR)
    I_gray = rgb2gray(I_rgb)
    #print(I_gray.shape)
    I_double=cropImage_v2(I_gray,1,550,150,720)#20,535,190,720)
    print(I_double.shape)
    imshow(I_double)
    I_down=DownSampling_v2(I_double,pixeldown)
    r,c=shape(I_down)
    I_vector=reshape(I_down, (r*c, 1)) 
    
    return I_vector
