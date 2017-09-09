"""
ObjectProperty
==============

This example demonstrates using an ObjectProperty (a Python object) to
reference the TextInput child widget created by the kv rule. After declaring
an ObjectProperty, you can hook it up to the child widget created in the kv 
rule e.g. 'display: entry'. Once that's done, you can easily reference the
TextInput property inside the calculate method.
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class CalcGridLayout(GridLayout):
    display = ObjectProperty(None)

    def calculate(self, dt):
        print(self.display.text)


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    CalculatorApp().run()
