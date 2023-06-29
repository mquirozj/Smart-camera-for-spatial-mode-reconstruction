# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:16:26 2022

@author: mquir
"""

from numpy import * #package to numerical calculations
from sklearn.datasets import fetch_openml
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pickle
from matplotlib.pyplot import * #package to plot
from processing import * 
from picamera import PiCamera
from time import sleep

filename = 'trained_model.sav'
NN = pickle.load(open(filename, 'rb'))

camara=PiCamera()
camara.resolution=(656,875)
camara.shutter_speed=6000
sleep(5)
camara.capture('/home/mquir/Documents/OAM/figure1.png')


pixel_down=30;
Imagen=r'/home/mquir/Documents/OAM/figure1.png'
I=readimage(Imagen,pixel_down)
imshow(I)
clase=NN.predict(I.T)

