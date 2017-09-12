from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window


Window.size = (800, 480)


class CustomDropDown(DropDown):
    pass


class Notes(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class TestApp(App):
    title = "Kivy Drop-Down List Demo"

    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    TestApp().run()
