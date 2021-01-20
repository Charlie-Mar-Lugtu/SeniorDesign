import arcade
import math
import random
import os
SPRITE_SCALING_PLAYER = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HelicopterNew"
class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.helicopter_list = None
        #player_sprite
        self.helicopter_sprite = None
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        #setup the player
        self.helicopter_list = arcade.SpriteList()
        self.helicopter_sprite = arcade.Sprite("Helicopter.png", SPRITE_SCALING_PLAYER)
        self.helicopter_sprite.center_x = 50
        self.helicopter_sprite.center_y = 50
        self.helicopter_list.append(self.helicopter_sprite)
    def on_draw(self):
        arcade.start_render()
        self.helicopter_list.draw()
    def on_mouse_motion(self, x, y, dx, dy):
        self.helicopter_sprite.center_x = x
        self.helicopter_sprite.center_y = y
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()