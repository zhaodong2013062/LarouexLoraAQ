import random

class TempSensor():

    def __init__(self):
        self.curr_value = 50

    def getValue(self):
        self.curr_value = self.curr_value + random.randint(-5, 5)
        return self.curr_value