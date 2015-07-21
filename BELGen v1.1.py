#!/usr/bin/python

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import time
import os

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 12)

r1 = 1
r2 = 100
v_read = adc.read_voltage(1)
v_batt = v_out1 * (r1 + r2) 


while (True):

    # clear the console
    os.system('clear')

    # read from adc channels and print to screen
    print ("Channel 1 Voltage Reading: %02f" % (v_read))

    # calculating voltage otherside of voltage divider to battery
    print ("Voltage out to battery: %02f" % (v_batt))
    
    # wait 0.5 seconds before reading the pins again
    time.sleep(0.5)
