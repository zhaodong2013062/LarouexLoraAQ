import adafruit_dht

class TempHumSensor():

    def __init__(self, dht_pin):
        self._dht_device = adafruit_dht.DHT22(dht_pin)
    
    def get_temp(self):
        return self._dht_device.temperature

    def get_hum(self):
        return self._dht_device.humidity