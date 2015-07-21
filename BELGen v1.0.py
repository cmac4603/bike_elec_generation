#!/usr/bin/python

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import os
import time

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 12)

v1 = adc.read_voltage(1)
v2 = adc.read_voltage(2)

def calcCurrent(inval):
    return ((inval) - (v1 / 2)) / 0.066

#c1 = float(vdd / calcCurrent(v2))

while (True):

    # clear the console
    os.system('clear')

    # read from adc channels and print to screen
    print ("Channel 1 voltage V: %02f" % v1)
    print ("Channel 1 current I: %02f" % calcCurrent(v2))
    #print ("Channel 1 resistance R: %02f" % c1)

    
    # wait 1 second before reading the pins again
    time.sleep(1)
