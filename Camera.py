#!/usr/bin/python

from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
today = datetime.now()
imgTime = today("%Y%m%d-%H%M%S")

#camera.start_preview()
#sleep(5)
camera.resolution = (3280, 2464)
camera.rotation = 90
camera.capture("/home/pi/Desktop/img%s.jpg" $ imgTime)
camera.stop_preview()