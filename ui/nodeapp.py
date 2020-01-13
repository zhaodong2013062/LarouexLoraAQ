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

class NodeApp(App):

    def build(self):
        # Set up the layout:
        layout = FloatLayout(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

        # Make the background gray:
        with layout.canvas.before:
            Color(.8,.8,.8,1)
            self.rect = Rectangle(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
                pos=layout.pos)

        self.is_c = False

        self.temp_sensor = TempSensor(50)
        self.hum_sensor = TempSensor(30)
        self.part_sensor = TempSensor(20)

        self.temp_gauge = Gauge(size_gauge = 200, pos=(50,100))
        self.hum_gauge = Gauge(size_gauge = 200, pos=(300,100))
        self.part_gauge = Gauge(size_gauge = 200, pos=(550,100))

        temp_label = Label(text='Temperature (F)', pos=(-250, 70), color=(0,0,0,1))
        hum_label = Label(text='Humidity (%)', pos=(0, 70), color=(0,0,0,1))
        part_label = Label(text='Particulates (%)', pos=(250, 70), color=(0,0,0,1))

        switch_button = Button(text='Stabilize/Unstabilize Temp', pos=(60, 50), size_hint=(0.24, 0.1))
        switch_button.bind(on_press=self.button_callback)

        layout.add_widget(self.temp_gauge)
        layout.add_widget(self.hum_gauge)
        layout.add_widget(self.part_gauge)
        layout.add_widget(temp_label)
        layout.add_widget(hum_label)
        layout.add_widget(part_label)
        layout.add_widget(switch_button)

        Clock.schedule_interval(lambda *t: self.new_values(), 0.3)

        return layout

    def button_callback(self, instance):
        if self.is_c:
            self.temp_gauge.unit*= 100
        else:
            self.temp_gauge.unit*= 1/100
        self.is_c = not self.is_c

    def new_values(self):
        self.temp_gauge.value = self.temp_sensor.getValue()
        self.hum_gauge.value = self.hum_sensor.getValue()
        self.part_gauge.value = self.part_sensor.getValue()


