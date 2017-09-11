from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty


class SingleScreen(BoxLayout):
    pass


class Change_Label(BoxLayout):
    _python_access = ObjectProperty(None)


class TestApp(App):

    def build(self):
        Clock.schedule_interval(self.Callback_Clock, 3)
        return SingleScreen()

    def Callback_Clock(self, dt):
        self.root.ids.gb._python_access.text = "I Changed It By Clock! dt=" + str(dt)


if __name__ == '__main__':
    TestApp().run()
