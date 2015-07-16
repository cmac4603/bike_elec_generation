#!/usr/bin/python

import ABE_ADCPi_FORK
from ABE_helpers import ABEHelpers
import os
import time

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ABE_ADCPi_FORK.ADCPi(bus, 0x68, 0x69, 12)

#
v1 = adc.read_voltage(1)
v2 = adc.read_voltage(2)
i1 = adc.calcCurrent(2,1)

def calcResistance(volt, curr):
    if (volt. curr):
            return float(0.0)  # returned a negative voltage so return 0
        else:
            resistance = float(volt/curr)
            return float(resistance)

while (True):

    # clear the console
    os.system('clear')

    # read from adc channels and print to screen
    print ("Channel 1 voltage V: %02f" % v1)
    print ("Channel 1 current I: %02f" % i1)
    print ("Channel 1 resistance R: %02f" % calcResistance(v1, i1))

    
    # wait 1 second before reading the pins again
    time.sleep(1)
