from kivy.app import App
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path


# Windowsは、C:/Windows/fonts
# Macは/System/Library/Fonts
# App().run()

resource_add_path('C:/Windows/fonts')
LabelBase.register(DEFAULT_FONT, 'msgothic.ttc')

class TextApp(App):
    def build(self):
        return Label(text='みなさんこんにちは')

TextApp().run()