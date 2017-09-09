"""
Widget animation
================

This example demonstrates using event dispatcher, on_complete to automatically
start another animation when the previous animation completed.
"""

from kivy.app import App
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty


class AnimateRecord(FloatLayout):

    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super(AnimateRecord, self).__init__(**kwargs)
        animation_record = Animation(angle=360, duration=2)
        animation_record += Animation(angle=360, duration=2)
        animation_record.repeat = True
        animation_record.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0


class AnimateButton(FloatLayout):

    def animate_button(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        animation_btn = Animation(pos=(100, 100), t='out_bounce')
        animation_btn += Animation(pos=(200, 100), t='out_bounce')
        animation_btn &= Animation(size=(500, 500))
        animation_btn += Animation(size=(100, 50))

        animation_btn.bind(on_complete=self.animation_complete)

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation_btn.start(instance)

    def animation_complete(self, widget, animation):
        self.remove_widget(animation)
        self.add_widget(AnimateRecord())


class AnimateApp(App):

    def build(self):
        return AnimateButton()


if __name__ == "__main__":
    AnimateApp().run()
