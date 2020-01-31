import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class ADC():

    def __init__(self, channel):
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1015(i2c)
        self.chan = chan = AnalogIn(ads, channel)

    def read_value(self):
        return chan.value

    def read_voltage(self):
        return chan.read_voltage

