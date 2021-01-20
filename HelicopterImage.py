"""
Helicopter Design The 1st
by Charlie Mar Lugtu
"""
import arcade
import math


"""Set constants for the screen size"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HellicopterDesign"

"""Contants for the Helicopter blades"""
###copied from "Radar Sweep Example"
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
RADIANS_PER_FRAME =7 #Rate of spinning blades
SWEEP_LENGTH = 52 #size of the wings
###copied and pasted from previous with modification
CENTER_X2 = SCREEN_WIDTH // 2
CENTER_Y2 = SCREEN_HEIGHT // 2
###copied and pasted from previous with modification
CENTER_X3 = SCREEN_WIDTH // 2
CENTER_Y3 = SCREEN_HEIGHT // 2
###copied and pasted from previous with modification
CENTER_X4 = SCREEN_WIDTH // 2
CENTER_Y4 = SCREEN_HEIGHT // 2
###Function###


def draw_helicopter(delta_time):
        """Olive Propeller Wing(copied from "Radar Sweep Example")"""
        draw_helicopter.angle += RADIANS_PER_FRAME #Making the blades spin
        x = SWEEP_LENGTH * math.sin(draw_helicopter.angle) + CENTER_X
        y = SWEEP_LENGTH * math.cos(draw_helicopter.angle) + CENTER_Y
        """Light_Green Propeller Wing(copied and
         pasted from previous with modification)"""
        draw_helicopter.angle2 += RADIANS_PER_FRAME
        x2 = SWEEP_LENGTH * math.sin(draw_helicopter.angle2) + CENTER_X2
        y2 = SWEEP_LENGTH * math.cos(draw_helicopter.angle2) + CENTER_Y2
        """Pink_Pearl Propeller Wing(copied and 
            pasted from previous with modification)"""
        draw_helicopter.angle3 += RADIANS_PER_FRAME
        x3 = SWEEP_LENGTH * math.sin(draw_helicopter.angle3) + CENTER_X3
        y3 = SWEEP_LENGTH * math.cos(draw_helicopter.angle3) + CENTER_Y3
        """Pink_Pearl Propeller Wing(copied and 
             pasted from previous with modification)"""
        draw_helicopter.angle4 += RADIANS_PER_FRAME
        x4 = SWEEP_LENGTH * math.sin(draw_helicopter.angle4) + CENTER_X4
        y4 = SWEEP_LENGTH * math.cos(draw_helicopter.angle4) + CENTER_Y4
        """Clear screen and start render process"""
        arcade.start_render()


        ###HelicopterImageCode####

        #BODY
        arcade.draw_rectangle_filled(400, 400, 30, 60,
                              arcade.color.RED_ORANGE)
        #FRONTWINDSHEILD

        arcade.draw_rectangle_filled(400, 423, 20, 15,
                              arcade.color.LIGHT_BLUE)

        #LEFTGUN
        arcade.draw_rectangle_filled(383, 409, 7, 30,
                              arcade.color.DARK_GREEN)
        #RIGHTGUN
        arcade.draw_rectangle_filled(418, 409, 7, 30,
                              arcade.color.DARK_GREEN)
        #MIDDLEGUN
        arcade.draw_rectangle_filled(400, 433, 7, 7,
                              arcade.color.DARK_GREEN)
        #TAIL
        arcade.draw_rectangle_filled(400, 344, 6, 55,
                              arcade.color.DARK_RED)

        arcade.draw_rectangle_filled(400, 330, 10, 20,
                              arcade.color.DARK_RED)

        #PROPELLER middle
        """arcade.draw_line(CENTER_X, CENTER_Y, x, y, arcade.color.OLIVE, 4)
        arcade.draw_line(CENTER_X2, CENTER_Y2, x2, y2, arcade.color.LIGHT_GREEN, 4)
        arcade.draw_line(CENTER_X3, CENTER_Y3, x3, y3, arcade.color.PINK_PEARL, 4)
        arcade.draw_line(CENTER_X4, CENTER_Y4, x4, y4, arcade.color.PURPLE, 4)"""
        arcade.draw_circle_filled(400, 400, 5, arcade.color.GREEN)
    #copied from "Radar Sweep Example"
draw_helicopter.angle = 0 #Olive wing
draw_helicopter.angle2 = 3.14 #Light_Green wing
draw_helicopter.angle3 =1.57 #Pink_Pearl wing
draw_helicopter.angle4 =4.71 #Purple wing
def main():
    """Open the window. Set the window title and dimensions"""
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    """Set the background color"""
    arcade.set_background_color(arcade.color.WHITE)
    """copied from "Radar Sweep Example" """
    arcade.schedule(draw_helicopter, 1 / 80)
    #draw_helicopter()
    """ Finish drawing and display the result"""
    arcade.finish_render()

    """ Keep the window open until the user hits the 'close' button"""
    arcade.run()

    # When done running the program, close the window.
    #arcade.close_window()
if __name__ == "__main__":
    main()