#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import lcddriver
from time import *

lcd = lcddriver.lcd()

print "argv1=",str(sys.argv[1])," argv2=",str(sys.argv[3])
lcd.lcd_display_string(sys.argv[1],int(sys.argv[2]))
lcd.lcd_display_string(sys.argv[3],int(sys.argv[4]))


