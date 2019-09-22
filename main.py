from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file("toolbox.kv")
Builder.load_file("drawingspace.kv")
Builder.load_file("generaloptions.kv")
Builder.load_file("statusbar.kv")
Builder.load_file("comicwidgets.kv")




class MyLayout(AnchorLayout):
    pass


class WeatherApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":   # prevents files from being run if file is imported (only import code from kivy)
    WeatherApp().run()    