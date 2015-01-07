#!/usr/bin/python
# -*- coding: utf-8 -*-


i2c_addr = 0x20

# import libraries
import smbus as smbus
import RPIO
from time import *
from subprocess import Popen, PIPE

#configure I2C bus for functions
i2c = smbus.SMBus(1)
c=0
while True:
    temp = i2c.read_byte( i2c_addr )
    if (temp != 0xff):
	print c, 'PCF8574 at address 0x{0:2x} READ 0x{1:2x}'.format( i2c_addr, temp )
	c+=1
    sleep(0.22)
