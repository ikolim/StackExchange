import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

import numpy as np

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivyagg')
from matplotlib import pyplot as plt
from kivy.garden.matplotlib import FigureCanvasKivyAgg


class MainScreen(Screen):

    ms_iptHpIdx = ObjectProperty(None)
    ms_btnToPoint = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        iptHpIdx = TextInput(text='', multiline=False, font_size=50)
        btnToPoint = Button(text='input')

        self.ms_iptHpIdx = iptHpIdx
        self.ms_btnToPoint = btnToPoint

        btnToPoint.bind(on_press=self.IptAct)

        layout = BoxLayout(orientation='vertical')  # syntax(padding=10, orientation='vertical')

        layout.add_widget(iptHpIdx)
        layout.add_widget(btnToPoint)
        layout.add_widget(canvas)

        self.add_widget(layout)

    def IptAct(self, btn):
        global HpHist
        self.ms_btnToPoint.text = 'Your input ' + self.ms_iptHpIdx.text

        try:
            val = int(self.ms_iptHpIdx.text)
            HpHist.append(self.ms_iptHpIdx.text)
            print('HpHistAf', HpHist)
        except ValueError:
            print("That's not an int!")

        print(HpHist)

        plt.clf()

        plt.plot(HpHist)
        canvas.draw_idle()


class TestKivyMatplotlib(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='MainPage'))
        return sm


if __name__ == '__main__':
    HpHist = []

    (fig, axe) = plt.subplots()
    canvas = fig.canvas
    TestKivyMatplotlib().run()
