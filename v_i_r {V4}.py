#!/usr/bin/python

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import os
import time

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 12)

#
v1 = adc.read_voltage(1)
v2 = adc.read_voltage(2)

def calcCurrent(inval):
    return ((inval) - 2.5) / 0.066


def calcResistance(value):
    return ((adc.read_voltage(1))/calcCurrent(v2))


while (True):

    # clear the console
    os.system('clear')

    # read from adc channels and print to screen
    print ("Voltage V: %02f" % v1)
    print ("Current I: %02f" % calcCurrent(v2))
    print ("Resistance R: %02f" % calcResistance(v1))

    
    # wait 1 second before reading the pins again
    time.sleep(1)
