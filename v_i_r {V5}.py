#!/usr/bin/python

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import os
import time

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 12)

# voltage reading from channel 1
v1 = adc.read_voltage(1)
# voltage reading from channel 2, used for current calc i2
v2 = adc.read_voltage(2)

# calculates current from channel preceded by 'i' (eg. i2)
# i2 = current calculated from adc channel 2 defined globally

def calccurrent(inval):
    global i
    i = ((inval) - 2.5) / 0.066


# calculates resistance using tow global variables
# voltage/current = r where v_channel = i_channel - 1
def calcresistance(v):
    global r
    r = (v/i)

while (True):

    # clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # print voltage on ch1
    print ("Voltage V: %02f" % adc.read_voltage(1))
    # print current on ch2
    print ("Current I: %02f" % calccurrent(v2))
    # print resistance calculated from channels 1 & 2
    print ("Resistance R: %02f" % calcresistance(v1))

    
    # wait 1 second before reading the pins again
    time.sleep(1)
