import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from ui.gauge import Gauge
import constants
from sensors.tempsensor import TempSensor
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

class SettingsScreen(Screen):

    def __init__(self, **kw):
        super(SettingsScreen, self).__init__(**kw)

        # Make the background gray:
        with self.canvas.before:
            Color(.8,.8,.8,1)
            self.rect = Rectangle(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
                pos=self.pos)

        temp_label = Label(text='Temperature (F)', pos=(-250, 70), color=(0,0,0,1))
        self.add_widget(temp_label)



