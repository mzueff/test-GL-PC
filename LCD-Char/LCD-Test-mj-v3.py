#!/usr/bin/python
# -*- coding: utf-8 -*-
import lcddriver
from time import *
from subprocess import Popen, PIPE



p = Popen('hostname -I', stdout=PIPE, shell=True)
out, err = p.communicate()
adres=out.strip()
print adres

lcd = lcddriver.lcd()

lcd.lcd_display_string("Hello world", 3)
lcd.lcd_display_string("My name is", 4)
lcd.lcd_display_string("Start!", 1)
lcd.lcd_display_string(adres, 2)


