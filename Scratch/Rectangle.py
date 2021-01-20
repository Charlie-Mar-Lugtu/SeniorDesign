import arcade
class Rectangle:
    def __init__(self, position_x, position_y,  length, width, color):
        self.position_x=position_x
        self.position_y=position_y
        self.length = length
        self.width = width
        self.color = color
    def draw(self):

        arcade.draw_rectangle_filled(self.position_x,self.position_y,
                                     self.length, self.width, self.color)

class Rectangle2:
    def __init__(self, position_x2, position_y2, length2, width2, color2):
        self.position_x2=position_x2
        self.position_y2=position_y2
        self.length2 = length2
        self.width2 = width2
        self.color2 = color2
    def draw(self):

        arcade.draw_rectangle_filled(self.position_x2,self.position_y2,
                                     self.length2, self.width2, self.color2)