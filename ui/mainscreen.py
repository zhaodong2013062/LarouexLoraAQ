import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from ui.gauge import Gauge
import constants
from sensors.tempsensor import TempSensor
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):

    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)

        with self.canvas.before:
            Color(.8,.8,.8,1)
            self.rect = Rectangle(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
                pos=self.pos)

        self.temp_sensor = TempSensor(50)
        self.hum_sensor = TempSensor(30)
        self.part_sensor = TempSensor(20)

        self.temp_gauge = Gauge(size_gauge = 200, pos=(50,100))
        self.hum_gauge = Gauge(size_gauge = 200, pos=(300,100))
        self.part_gauge = Gauge(size_gauge = 200, pos=(550,100))

        temp_label = Label(text='Temperature (F)', pos=(-250, 70), color=(0,0,0,1))
        hum_label = Label(text='Humidity (%)', pos=(0, 70), color=(0,0,0,1))
        part_label = Label(text='Particulates (%)', pos=(250, 70), color=(0,0,0,1))

        self.add_widget(self.temp_gauge)
        self.add_widget(self.hum_gauge)
        self.add_widget(self.part_gauge)
        self.add_widget(temp_label)
        self.add_widget(hum_label)
        self.add_widget(part_label)

        Clock.schedule_interval(lambda *t: self.new_values(), 0.3)

    def new_values(self):
        self.temp_gauge.value = self.temp_sensor.getValue()
        self.hum_gauge.value = self.hum_sensor.getValue()
        self.part_gauge.value = self.part_sensor.getValue()


