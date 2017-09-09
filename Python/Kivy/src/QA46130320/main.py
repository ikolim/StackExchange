from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty


class RootWidget(BoxLayout):
    ASSETS = "/home/iam/Pictures/Images/"
    os = DictProperty({})
    os = {
        'kivy': ("{}{}".format(ASSETS, "Kivy/kivy-logo-black-64.png")),
        'linux': ("{}{}".format(ASSETS, "Kivy/linux.png")),
        'mac': ("{}{}".format(ASSETS, "Kivy/macosx.png")),
        'windows': ("{}{}".format(ASSETS, "Kivy/windows.png")),
        'raspberrypi': ("{}{}".format(ASSETS, "Kivy/raspberrypi.png"))
    }


class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    TestApp().run()
