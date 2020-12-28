# RPiUVCamera
This a simple UV camera project using a Raspberry Pi and the NoIR camera module v2. I used the NoIR module so there is no additional filter added to the camera (normal camera module will have an infrared filter). A 3.5" touch screen provides display and interface for the camera. An inexpensive UV pass filter (passing 360-420 nm) removes IR and most of the visible light spectrum. 

## Parts List
Raspberry Pi 4B<br/>
Raspbian Desktop<br/>
NoIR Camera Module<br/>
Rosco UV Pass Glass Filter<br/>
Landzo 3.5" Touchscreen<br/>
8 gb Flash Card<br/>

## Python Script
The python script is on the RPi desktop that is executable which sets the resolution, rotation, and names the image based on the current date and time. Be sure you enable the camera module using rasp-config (command) or Raspberry Pi Configuration (menu). Also, create a "UV Photos" folder on the Desktop (or alter the path in the script).

## Case
I printed a modified version of https://www.thingiverse.com/thing:3735600 to hold the filter. My current version is in need of some major refinement. 
