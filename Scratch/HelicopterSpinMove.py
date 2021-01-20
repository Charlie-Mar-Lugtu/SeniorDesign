import arcade
import math
from Scratch.Rectangle import Rectangle
from Scratch.Rectangle import Rectangle2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HelicopterSpinMove"

CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
RADIANS_PER_FRAME = 0.00
SWEEP_LENGTH = 52

"""CENTER_X2 = SCREEN_WIDTH // 2
CENTER_Y2 = SCREEN_HEIGHT // 2
###copied and pasted from previous with modification
CENTER_X3 = SCREEN_WIDTH // 2
CENTER_Y3 = SCREEN_HEIGHT // 2
###copied and pasted from previous with modification
CENTER_X4 = SCREEN_WIDTH // 2
CENTER_Y4 = SCREEN_HEIGHT // 2"""
class Line:
    def __init__(self, start_x, start_y, end_x, end_y, color, width):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color
        self.width = width
    def draw(self):
        arcade.draw_line(self.start_x,self.start_y,
                         self.end_x,self.end_y,
                         self.color,self.width)
"""class Circle:
    def __init__(self, postion_x, position_y, radius, color):
        self.position_x = postion_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y,
                                  self.radius, self.color)"""

class HelicopterGame(arcade.Window):
    """Main class"""

    def __init__(self, width, height, title):
        super().__init__(width,height,title)
        self.rectangle = None
        self.rectangle2 = None
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)
        """copied from "drawing_text.py" """
        self.helicopter_angle = 0
        """self.helicopter_angle2=3.14
        self.helicopter_angle3=1.57
        self.helicopter_angle4=4.71"""
        #Create Helicopter

        self.rectangle = Rectangle(400, 400, 30, 60,
                                   arcade.color.RED_ORANGE)
        self.rectangle2 = Rectangle2(400, 423, 20, 15,
                                   arcade.color.LIGHT_BLUE)
        """self.rectangle3 = Rectangle(383, 409, 7, 30,
                                    arcade.color.DARK_GREEN)
        self.rectangle4 = Rectangle(418, 409, 7, 30,
                                    arcade.color.DARK_GREEN)
        self.rectangle5 = Rectangle(400, 433, 7, 7,
                                    arcade.color.DARK_GREEN)
        self.rectangle6 = Rectangle(400, 344, 6, 55,
                                    arcade.color.DARK_RED)
        self.rectangle7 = Rectangle(400, 330, 10, 20,
                                    arcade.color.DARK_RED)"""
       # self.circle = Circle(400, 400, 5, arcade.color.GREEN)

    def on_draw(self):
        arcade.start_render()

        #BODY

        self.rectangle.draw()
        #WINDSHEILD

        self.rectangle2.draw()
        #LEFTGUN

        """self.rectangle3.draw()
        #RIGHTGUN

        self.rectangle4.draw()
        #MIDDLEGUN

        self.rectangle5.draw()
        #TAIL

        self.rectangle6.draw()

        self.rectangle7.draw()"""
        #WINGS
            #Olive wing
        """copied from "radar_sweep.py" with my modifications"""
        self.helicopter_angle += RADIANS_PER_FRAME
        self.x = SWEEP_LENGTH * math.sin(self.helicopter_angle) + CENTER_X
        self.y = SWEEP_LENGTH * math.cos(self.helicopter_angle) + CENTER_Y
        self.line = Line(CENTER_X, CENTER_Y, self.x, self.y,
                         arcade.color.OLIVE, 4)
        self.line.draw()
            #Light_Green wing
        """self.helicopter_angle2 += RADIANS_PER_FRAME
        self.x2 = SWEEP_LENGTH * math.sin(self.helicopter_angle2) + CENTER_X2
        self.y2 = SWEEP_LENGTH * math.cos(self.helicopter_angle2) + CENTER_Y2
        self.line2 = Line(CENTER_X2, CENTER_Y2, self.x2, self.y2,
                          arcade.color.LIGHT_GREEN, 4)
        self.line2.draw()
            #Pink_Pearl wing
        self.helicopter_angle3 += RADIANS_PER_FRAME
        self.x3 = SWEEP_LENGTH * math.sin(self.helicopter_angle3) + CENTER_X3
        self.y3 = SWEEP_LENGTH * math.cos(self.helicopter_angle3) + CENTER_Y3
        self.line3 = Line(CENTER_X3, CENTER_Y3, self.x3, self.y3,
                          arcade.color.PINK_PEARL, 4)
        self.line3.draw()
            #Purple wing
        self.helicopter_angle4 += RADIANS_PER_FRAME
        self.x4 = SWEEP_LENGTH * math.sin(self.helicopter_angle4) + CENTER_X4
        self.y4 = SWEEP_LENGTH * math.cos(self.helicopter_angle4) + CENTER_Y4
        self.line4 = Line(CENTER_X4, CENTER_Y4, self.x4, self.y4,
                          arcade.color.PURPLE, 4)
        self.line4.draw()"""
        #CENTER SPIN

        #self.circle.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.rectangle.position_x = x
        self.rectangle.position_y = y
        self.rectangle2.position_x2 = x
        self.rectangle2.position_y2 = y+23

        self.line = x
        self.line = y




    """def on_mouse_motion(self, x, y,
                        x2, y2,
                        x3, y3,
                        x4, y4,
                        x5, y5,
                        x6, y6,
                        x7, y7,
                        dx, dy,
                        dx2, dy2,
                        dx3, dy3,
                        dx4, dy4,
                        dx5, dy5,
                        dx6, dy6,
                        dx7, dy7,):
        x = 400
        y = 400
        x2 = 400
        y2 = 423
        x3 = 383
        y3 = 409
        x4 = 418
        y4 = 409
        x5 = 400
        y5 = 433
        x6 = 400
        y6 = 344
        x7 = 400
        y7 = 330
        self.rectangle.position_x = x
        self.rectangle.position_y = y
        self.rectangle2.position_x2 = x2
        self.rectangle2.position_y2 = y2
        self.rectangle3.position_x3 = x3
        self.rectangle3.position_y3 = y3
        self.rectangle4.position_x4 = x4
        self.rectangle4.position_y4 = y4
        self.rectangle5.position_x5 = x5
        self.rectangle5.position_y5 = y5
        self.rectangle6.position_x6 = x6
        self.rectangle6.position_y6 = y6
        self.rectangle7.position_x7 = x7
        self.rectangle7.position_y7 = y7

        self.line.start_x = x
        self.line.start_y = y
        self.line2.start_x = x
        self.line2.start_y = y
        self.line3.start_x = x
        self.line3.start_y = y
        self.line4.start_x = x
        self.line4.start_y = y

        self.circle.position_x = x
        self.circle.position_y = y"""

def main():
    window = HelicopterGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()