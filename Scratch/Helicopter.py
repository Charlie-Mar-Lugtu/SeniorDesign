import arcade
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "HELICOPTER(ALT)"
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
RADIANS_PER_FRAME = 700 #Rate of spinning blades
SWEEP_LENGTH = 52 #size of the wings

class Propeller:
    def __init__(self, position_x, position_y, radius, color):


        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y,
                                  self.radius, self.color)
"""class Wing:
    def __init__(self, start_x, start_y, end_x, end_y, color, width):
        self.start_x=start_x
        self.start_y=start_y
        self.end_x=end_x
        self.end_y=end_y
        self.color=color
        self.width=width

    def draw(self):
        arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y, self.color, self.width)"""

"""def on_wing(delta_time):
    on_wing.angle += RADIANS_PER_FRAME
    end_x = SWEEP_LENGTH * math.sin(on_wing.angle) + CENTER_X
    end_y = SWEEP_LENGTH * math.cos(on_wing.angle) + CENTER_Y
on_wing.angle = 0"""
class Helicopter:

    def __init__(self, position_x, position_y, length, width, color):
        self.position_x=position_x
        self.position_y=position_y
        self.length = length
        self.width = width
        self.color = color
    def draw(self):

        arcade.draw_rectangle_filled(self.position_x,self.position_y,
                                     self.length, self.width, self.color)

class MyGame(arcade.Window):
    """Main class"""
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)


        # BODY

        self.helicopter1 = Helicopter(300, 300, 30, 60,
                                 arcade.color.RED_ORANGE)
        # FRONTWINDSHEILD
        self.helicopter2 = Helicopter(300, 323, 20, 15,
                                 arcade.color.LIGHT_BLUE)

        # LEFTGUN
        self.helicopter3 = Helicopter(283, 309, 7, 30,
                                  arcade.color.DARK_GREEN)

        # RIGHTGUN

        self.helicopter4 = Helicopter(318, 309, 7, 30,
                                  arcade.color.DARK_GREEN)

        # MIDDLEGUN
        self.helicopter5 = Helicopter(300, 333, 7, 7,
               arcade.color.DARK_GREEN)

        # TAIL
        self.helicopter6 = Helicopter(300, 244, 6, 55,
                                  arcade.color.DARK_RED)
        self.helicopter7 = Helicopter(300, 230, 10, 20,
                                  arcade.color.DARK_RED)
        #propeller middle
        self.propeller = Propeller(300,300,5,arcade.color.GREEN)
     #   self.wing = Wing(CENTER_X, CENTER_Y, end_y, end_y, arcade.color.OLIVE, 4)

    def on_draw(self):


        arcade.start_render()
        self.helicopter1.draw()
        self.helicopter2.draw()
        self.helicopter3.draw()
        self.helicopter4.draw()
        self.helicopter5.draw()
        self.helicopter6.draw()
        self.helicopter7.draw()
        #arcade.draw_line(CENTER_X, CENTER_Y, x, y, arcade.color.OLIVE, 4)
        self.propeller.draw()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()