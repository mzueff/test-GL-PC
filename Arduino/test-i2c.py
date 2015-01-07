import smbus
import time
import RPIO

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

# Interrupt Pin
PIN_INT=17
RPIO.setup(PIN_INT, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)


def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

def gpio_callback(gpio_id, val):
    R1 = 100000.0
    R2 = 10000.0
    number = readNumber()
    vout = (number * 5.0) / 1023.0
    vin = vout / (R2/(R1+R2))
    print "Arduino received a voltage ", vin
    print 


RPIO.add_interrupt_callback(PIN_INT, gpio_callback, pull_up_down=RPIO.PUD_UP, threaded_callback=False, debounce_timeout_ms=50)

RPIO.wait_for_interrupts()
