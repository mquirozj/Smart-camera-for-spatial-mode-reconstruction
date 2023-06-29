# -*- coding: utf-8 -*-
"""
Created on Tue Dec 8 14:50:26 2022

@author: mquir
"""

from numpy import * #package to numerical calculations
from picamera import PiCamera
from time import sleep


camara=PiCamera()
camara.resolution=(656,875)
camara.shutter_speed=6000

for i in range(100):
	name='/home/tomas/Documents/OAM/figure'+str(i)+'.png'
	camara.capture(name)
	sleep(5)

