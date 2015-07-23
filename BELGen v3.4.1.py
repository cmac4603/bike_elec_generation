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
EXIT_BUTTON = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(EXIT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_press = GPIO.input(BUTTON_PIN)

# voltage reading from channel 1 (v_supply) / 2, used for calccurrent()
v_i = (adc.read_voltage(1)) /2
# voltage reading from channel 1 (v_supply), used for calccurrent()
v1 = (adc.read_voltage(1))

# calculates current from channel labelled 'v_i'
# i = current calculated from adc channel 1 defined globally
def calccurrent(inval):
    global i
    i = ((inval) - v_i) / 0.066
    return ((inval) - v_i) / 0.066
    
# calculates resistance using two global variables
# voltage/current = r
def calcresistance(volts):
    global r
    r = (volts/i)
    return (volts/i)

def quit_program(channel):
    print('Exit button pressed, quiting program...')
    GPIO.cleanup()
    time.sleep(1)
    exit()


def start():
    print('Voltage, Current & Resistance v3.4.1 2015')
    print('Press the green button for voltage, current, and resistance...')
    print('Or the red button to quit.')
    GPIO.add_event_detect(EXIT_BUTTON, GPIO.FALLING, callback=quit_program)
    try:
        GPIO.wait_for_edge(24, GPIO.FALLING)
        print ("Voltage V: %02f" % adc.read_voltage(1), 'V')
        # print current on ch2
        print ("Current I: %02f" % calccurrent(v1))
        # print resistance calculated from channels 1 & 2
        print ("Resistance R: %02f" % calcresistance(v1))
        # key debounce
        time.sleep(0.2)
        GPIO.cleanup()
    except KeyboardInterrupt:
       GPIO.cleanup()

start()
