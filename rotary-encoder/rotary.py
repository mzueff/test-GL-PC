#!/usr/bin/python
import os
import RPIO
from time import sleep
RPIO.setup(22, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
RPIO.setup(27, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
encoder_A_prev= True
while True:
    # A pin
    encoder_A=RPIO.input(22)
    #B pin
    encoder_B=RPIO.input(27)
    #if((encoder_A == False) and (encoder_A_prev==True)):
    if(encoder_B == True and encoder_A == False):
	    print "BBBBBBBBBBBBBBBBB"
    elif(encoder_B == False and encoder_A == True):
	    print "A"
    encoder_A_prev = encoder_A
    #print "A=",encoder_A, "B=", encoder_B, encoder_A_prev 
    sleep(0.05)