import wiringpi
from sensors.adc import ADC
from statistics import median

class PMSensor:
    def __init__(self, led_pin, adc_channel, sampling_time=280, delta_time=40, sleep_time=9680):
        self._adc = ADC(adc_channel)
        self.led_pin = led_pin
        
        wiringpi.wiringPiSetupGpio() 
        wiringpi.pinMode(led_pin, 1)
        wiringpi.digitalWrite(led_pin, 0)

        self.sampling_time = sampling_time
        self.delta_time = delta_time
        self.sleep_time = sleep_time

    
    def get_value(self):
        wiringpi.digitalWrite(self.led_pin, 1) # power on the LED
        wiringpi.delayMicroseconds(self.sampling_time) 
        wiringpi.delayMicroseconds(self.delta_time)
        vo_measured = self._adc.read_voltage() # read the dust value
        wiringpi.digitalWrite(self.led_pin, 0) # turn the LED off
        
        # linear eqaution taken from http://www.howmuchsnow.com/arduino/airquality/ (Chris Nafis (c) 2012)
        dust_density = 0.17 * vo_measured - 0.1

        return dust_density
        
    
    def get_sequence(self):
        readings = []

        for i in range(10):
            readings.append(self.get_value())
            wiringpi.delayMicroseconds(self.sleep_time) # wait 9.68ms before the next sequence is repeated

        return median(readings)