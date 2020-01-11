import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from ui.gauge import Gauge

class NodeApp(App):

    def build(self):
        # Set up the layout:
        layout = FloatLayout(size=(800,600))

        # Make the background gray:
        with layout.canvas.before:
            Color(.8,.8,.8,1)
            self.rect = Rectangle(size=(800,600), pos=layout.pos)

        temp_gauge = Gauge(size_gauge = 200, pos=(50,200))
        hum_gauge = Gauge(size_gauge = 200, pos=(300,200))
        part_gauge = Gauge(size_gauge = 200, pos=(550,200))
        layout.add_widget(temp_gauge)
        layout.add_widget(hum_gauge)
        layout.add_widget(part_gauge)

        return layout