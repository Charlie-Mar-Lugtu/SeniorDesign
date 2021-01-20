
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "HelicopterMovement"


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        #self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        #self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        #self.coin_list = arcade.SpriteList()

        # Score
        #self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("Helicopters/Wing0.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)



    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.player_list.draw()



    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()