import Adafruit_DHT

class TempHumSensor():

    def __init__(self, dht_model, dht_pin):
        self.dht_model = dht_model
        self.dht_pin = dht_pin

    def get_values(self):
        return Adafruit_DHT.read_retry(self.dht_model, self.dht_pin)