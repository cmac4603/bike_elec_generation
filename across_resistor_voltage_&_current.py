#!/usr/bin/python

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import os
import time

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 12)

v_r1 = adc.read_voltage(1)

def calcCurrent(inval):
    return ((inval) - v_r1) / 0.066

while (True):

    # clear the console
    os.system('clear')

    # read from adc channels and print to screen
    print ("Channel 1 voltage V: %02f" % v_r1)
    print ("Channel 1 current I: %02f" % calcCurrent(adc.read_voltage(1)))
    print ("Channel 1 resistance R: %02f" % v_r1/calcCurrent(adc.read_voltage(1))

    
    # wait 1 second before reading the pins again
    time.sleep(1)
