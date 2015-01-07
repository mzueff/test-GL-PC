i2c_addr = 0x20

# import libraries
import smbus as smbus
import RPIO
from time import *
i2c = smbus.SMBus(1)

byte=[0x10, 0x20, 0x30, 0x40]

c=0;
while True:
    temp = i2c.write_byte( i2c_addr, byte[c] )
    print c, temp
    if  c < 3:
	c+=1
    else:
	c=0
    sleep(0.2)