# RPiUVCamera
This a simple UV camera project using a Raspberry Pi and the NoIR camera module v2. I used the NoIR module so there is no additional filter added to the camera (normal camera module will have an infrared filter). Originally, I used a 3.5" touch screen, but this was cumbersome. Instead, I use an old tablet running VNC client and connect to the Raspberry Pi via wifi hotspot. An [inexpensive UV pass filter (passing 360-420 nm)](https://www.bhphotovideo.com/c/product/1010867-REG/rosco_120336607508_2x2_permacolor_glass_filter.html) removes IR and most of the visible light spectrum. 

## Parts List
Raspberry Pi 4B<br/>
Raspbian Desktop<br/>
NoIR Camera Module<br/>
Rosco UV Pass Glass Filter<br/>
8 gb Flash Card<br/>

## Bash Script
Originally, I used the python script, but switched to a simple Bash script on the RPi desktop that is executable which sets white balance to sun and names the image based on the current date and time ("img_YearMonthDay_HourMinuteSec.jpg"). Be sure you enable the camera module using rasp-config (command) or Raspberry Pi Configuration (menu).

## Case STL Files
This is a modified version of https://www.thingiverse.com/thing:3735600 to hold the filter. My current version is in need of some major refinement. 

## License
RPiUVCamera follows the MIT License. However, the case STL files are licensed under [CC-BY-NC-SA-4.0](https://github.com/PlantEcology/RPiUVCamera/edit/main/CC-BY-NC-SA-4.0), thus are restricted for commercial use.
