import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Aliens"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()


arcade.draw_rectangle_filled(400, 400, 90, 40, arcade.color.ORANGE_PEEL)
arcade.draw_circle_filled(400, 417, 30, arcade.color.LIGHT_BLUE)
arcade.draw_line(365, 365, 380, 380, arcade.color.BLACK, 2)
arcade.draw_line(395, 365, 380, 380, arcade.color.BLACK, 2)
arcade.draw_line(410, 366, 425, 380, arcade.color.BLACK, 2)
arcade.draw_line(440, 366, 425, 380, arcade.color.BLACK, 2)

arcade.draw_line(200, 183, 200, 200, arcade.color.RED, 5)

arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()