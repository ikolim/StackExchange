import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


Config.set("graphics", "width", "800")
Config.set("graphics", "height", "50")
Config.set("graphics", "borderless", "0")
Config.set("graphics", "resizable", "0")


class SQLite3KivyDemo(BoxLayout):

    def __init__(self, **kwargs):
        super(SQLite3KivyDemo, self).__init__(**kwargs)

    def db_query(self):
        connection = sqlite3.connect("company.db")

        cursor = connection.cursor()

        sql_command = """SELECT * FROM employee WHERE birth_date = "{}";""".format(self.ids.sel_date.text)
        cursor.execute(sql_command)

        result = cursor.fetchall()

        for row in result:
            print(row)


class TestApp(App):
    title = "Kivy & SQLite3 Demo"

    def build(self):
        return SQLite3KivyDemo()


if __name__ == "__main__":
    TestApp().run()
