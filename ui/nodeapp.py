import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from ui.mainscreen import MainScreen
from ui.settingsscreen import SettingsScreen
import constants
from kivy.clock import Clock

class NodeApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.ms = MainScreen(name="MainScreen")
        self.ss = SettingsScreen(name="SettingsScreen")
        self.sm.add_widget(self.ss)
        self.sm.add_widget(self.ms)

        self.next_screen = 1
        
        print(self.sm.screen_names)
        Clock.schedule_interval(lambda *t: self.switch_screens(), 5)
        return self.sm

    def switch_screens(self):
        self.sm.current = self.sm.next()