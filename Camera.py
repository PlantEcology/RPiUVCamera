#!/usr/bin/python

from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
today = datetime.now()
imgTime = today.strftime("%Y%m%d-%H%M%S")

camera.resolution = (3280, 2464)
camera.rotation = 90
camera.capture("/home/pi/Desktop/img%s.jpg" $ imgTime)
