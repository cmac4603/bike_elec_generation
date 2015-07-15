from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 12)

v1 = adc.read_voltage(1)
v2 = adc.read_voltage(2)

class CurrentCalculator:
    def calcCurrent(inval):
        return ((inval) - v1) / 0.066

    
    print ("Channel 1 current I: %02f" % calcCurrent(v2))
