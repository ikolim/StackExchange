from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial


class MyScreenManager(ScreenManager):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class SwitchingScreenApp(App):

    def build(self):
        root_widget = MyScreenManager()
        Clock.schedule_once(partial(self.screen_switch_one, sm=root_widget), 2)
        Clock.schedule_once(partial(self.screen_switch_two, sm=root_widget), 4)
        Clock.schedule_once(partial(self.screen_switch_three, sm=root_widget), 6)
        Clock.schedule_once(partial(self.screen_switch_four, sm=root_widget), 8)
        Clock.schedule_once(partial(self.screen_switch_one, sm=root_widget), 10)
        return root_widget

    def screen_switch_one(dt, *args, sm):
        sm.current = '_first_screen_'

    def screen_switch_two(dt, *args, sm):
        sm.current = '_second_screen_'
        sm.ids.first_screen_id.ids.first_screen_label.text = "Hi I'm The Fifth Screen"

    def screen_switch_three(dt, *args, sm):
        sm.current = '_third_screen_'

    def screen_switch_four(dt, *args, sm):
        sm.current = '_fourth_screen_'


if __name__ == "__main__":
    SwitchingScreenApp().run()
