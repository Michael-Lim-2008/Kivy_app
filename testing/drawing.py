from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingBoard(RelativeLayout):
    pass




# gets DrawingTest (without App), decapitalise, then find the file aka drawingtest.kv
class DrawingTestApp(App):
    def build(self):
        return DrawingBoard()

if __name__ == "__main__":
    DrawingTestApp().run()           