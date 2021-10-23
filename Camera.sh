#!/bin/bash

raspistill --awb sun -o ~/Desktop/img.jpg
mv ~/Desktop/img.jpg "$(date +"img_%Y%m%d_%H%M%S.jpg"):
