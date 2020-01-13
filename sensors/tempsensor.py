import random

class TempSensor():

    def __init__(self, set_value):
        self.curr_value = set_value

    def getValue(self):
        return self.curr_value + random.randint(-5, 5)