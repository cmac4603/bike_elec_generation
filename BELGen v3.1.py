#!/usr/bin/python

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import os
import time
import RPi.GPIO as GPIO

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 12)

# Configure the GPIO pins
BUTTON_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# voltage reading from channel 1
v1 = adc.read_voltage(1)
# voltage reading from channel 2, used for current calc i2
v2 = adc.read_voltage(2)
vref4c = (adc.read_voltage(1)) / 2
# calculates current from channel preceded by 'i' (eg. i2)
# i2 = current calculated from adc channel 2 defined globally

def calccurrent(inval):
    global i
    i = ((inval) - 1.65) / 0.066
    return ((inval) - 1.65) / 0.066
    
# calculates resistance using two global variables
# voltage/current = r
def calcresistance(v_ref):
    global r
    r = (v_ref/i)
    return (v_ref/i)

def start():
    print('Voltage, Current & Resistance v7 2015')

try:
    if v1 == 0:
        print('Error: No reading on channel 1')
        print('Waiting 5 seconds...')
        time.sleep(5)
    if v2 == 0:
            print('Error: No reading on channel 2')
            print('Waiting 5 seconds...')
            time.sleep(5)
    elif GPIO.input(BUTTON_PIN) == False:
        print ("Voltage V: %02f" % adc.read_voltage(1))
        # print current on ch2
        print ("Current I: %02f" % calccurrent(v1))
        # print resistance calculated from channels 1 & 2
        print ("Resistance R: %02f" % calcresistance(v1))
        # key debounce
        time.sleep(10)
    elif GPIO.input(BUTTON_PIN) == True:
        print('Press Button')
    else:
        print('WTF!')
finally:
    print('Cleaning up GPIO')
    GPIO.cleanup()
