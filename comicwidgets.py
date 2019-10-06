from kivy.uix.relativelayout import relativelayout
from kivy.graphics import Line

class DraggableWidget(RelativeLayout):
    def __init__(self):
        self.selected = None
        super().__init__()


    def select(self):
        self.ix = self.center_x
        self.iy = self.center_x   #ix/y is the thing the user is touching
        with self.canvas
        self.selected = line(rectangle = (0,0,self.width,self.height),dash_offset=2)
#                                                                       ^ the dotted rectangle(the amount of dots)

    def on_touch_down(self,touch):
        if self.collide_point(self.x,self.y):
            self.select()
            return True  
        return super()on_touch_down(touch)




    def on_touch_move(self,touch):
        x = self.parent.to_parent(touch.x,touch.y)[0]
        y = self.parent.to_parent(touch.x,touch.y)[1] 
        if self.selected = True and self.parent.collide_point(x-self.width/2,y-self.height/2    ):
            return True



        # if is touch
    def translate(self,x,y):
        self.center_x = self.ix
        self.center_y = self.iy
        self.ix += x
        self.iy = y
    def on_touch_up(self,touch):
        if self.selected == True:
            self.unselect()
            return True
        return super().on_touch-up(touch)  


    def unselect(self):
        if selected == True:
            self.canvas.remove(slef.selected)
            self.selected = None


class Stickman(DraggableWidget):
    pass              


        