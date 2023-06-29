# -*- coding: utf-8 -*-
"""
Created on Thu Dec  13 11:49:33 2022

@author: mquir
%"""
#pip install opencv-python

from numpy import * #package to numerical calculations
from matplotlib.pyplot import * #package to plot
import glob #read files from a directory with extension png
import cv2 #read images
from skimage.color import rgb2gray #from rgb to gray



def cropImage_v2(Im,alto_sup,alto_inf,ancho_izq,ancho_der):
    r,c=shape(Im)
    I=Im[alto_sup:alto_inf,ancho_izq:ancho_der]
    return I

def DownSampling_v2(FieldFinal,SquareSize):
    OutPixel,OutPixel2=shape(FieldFinal)
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
            Im=FieldFinal[ini_m:fin_m,ini_n:fin_n]
            FieldD[m,p]=sum(sum(Im))/(SquareSize**2)
    return FieldD

def readimages(Direccion,Observaciones,NumeroClases,IndiceClase,pixeldown):    
    Target=zeros([NumeroClases,Observaciones])
    imgPath=Direccion
    files = glob.glob(imgPath)
    count=0;
    
    for j in range(Observaciones):
        Nameimage=files[j]
        I_rgb=cv2.imread(Nameimage, cv2.IMREAD_COLOR)
        I_gray = rgb2gray(I_rgb)
        I_double=cropImage_v2(I_gray,1,550,150,720)#20,535,190,720)
        imshow(I_double)
        I_down=DownSampling_v2(I_double,pixeldown)
        #print(I_gray)
        if j==0:
            r,c=shape(I_down)
            I_vector=zeros([r*c,Observaciones])
            I_vector[0:(r*c),count:count+1]=reshape(I_down, (r*c, 1)) 
        else:
            I_vector[0:(r*c),count:count+1]=reshape(I_down, (r*c, 1)) 
        Target[IndiceClase,count]=1
        count=count+1
    #imshow(I_down)
    return I_vector,Target
    
#************************************Main**************************************

Name=list(range(6))
#Laguerre-Gauss
Name[0]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\V1_P_p3\*.png'
Name[1]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\Vm1_P_p3\*.png'
Name[2]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\V2_P_p3\*.png'
Name[3]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\Vm2_P_p3\*.png'


#Name[0]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\V1_P\*.png'
#Name[1]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\Vm1_P\*.png'
#Name[2]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\V2_P\*.png'
#Name[3]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\Vm2_P\*.png'
#Name[4]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\V5_P\*.png'
#Name[5]=r'C:\Users\mquir\Desktop\NeuralNetworkRaspBerry\DatasetRaspPot03\Vm5_P\*.png'




NumClasses=4
Observ=100
pixel_down=20
NumberClass=1
Input=zeros([756,NumClasses*Observ])#289
Target=zeros([NumClasses,NumClasses*Observ])


for k in range(NumClasses):
    print(k)
    I,T=readimages(Name[k],Observ,NumClasses,k,pixel_down)
    Input[:,Observ*k:Observ*(k+1)]=I
    Target[:,Observ*k:Observ*(k+1)]=T


savetxt('dataI.csv', Input, delimiter=',')
savetxt('dataT.csv', Target, delimiter=',')
    
    
    
    