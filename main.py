from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Привет, уродец",halign="center")


MainApp().run()
if __name__ == '__main__':
    MainApp().run()