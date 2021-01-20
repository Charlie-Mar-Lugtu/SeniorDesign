import random
import arcade
import os
import math


OFFSCREEN_SPACE = 300
BAD_GUY_COUNT = 3
SPRITE_SCALING_ROTOR = 0.4
SPRITE_SCALING_BULLET = 0.5
PLAYER_BULLET_SPEED = 5
ENEMY_BULLET_SPEED = 4
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Rotate Rotor"
SPRITE_SCALING_PLAYER = 0.5
INSTRUCTIONS = 0
GAME_RUNNING = 2
GAME_OVER = 3


class Rotor(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)
        self.angle = 0
        self.change_angle = -20

    def update(self):
        self.angle += self.change_angle

class EnemySprite(arcade.Sprite):

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0

    def reset_pos(self):


        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)
    def update(self):

        super().update()
        self.center_y -= 1.5
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self,):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        #BACKGROUND INITIALIZE
        self.background = None

        # SPRITE INITIALIZE
        self.rotor_list = None
        self.player_sprite = None
        self.player_list = None
        self.all_sprites_list = None
        self.blackbullet_list = None
        self.redbullet_list = None
        self.enemy1_list = None
        self.enemy1_sprite = None
        self.enemy2_list = None
        self.enemy2_sprite = None

        #INITIALIZE SCORES
        self.score = 0

        #INITIALIZE INSTRUCTIONS
        self.current_state = INSTRUCTIONS


        #WHEN MOUSE CURSUR GOES INTO THE GAME
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        #SPRITES
        self.score=0
        self.all_sprites_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite()
        self.rotor_list = arcade.SpriteList()

        self.blackbullet_list = arcade.SpriteList()
        self.redbullet_list = arcade.SpriteList()
        self.enemy1_list = arcade.SpriteList()
        self.enemy1_sprite = arcade.Sprite()
        self.enemy2_list = arcade.SpriteList()
        self.enemy2_sprite = arcade.Sprite()


        #SETUP BACKGROUND
        self.background = arcade.load_texture("Forest2.jpg")

        #SETUP PLAYER
        self.player_sprite = arcade.Sprite("Helicopters/Helicopter.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 47.125
        self.all_sprites_list.append(self.player_sprite)
        self.player_list.append(self.player_sprite)


        #SETUP ROTOR
        self.rotor = Rotor("Helicopters/Rotor.png", SPRITE_SCALING_ROTOR)
        self.rotor.center_x = 400
        self.rotor.center_y = 71
        self.rotor.angle = math.sin(0)
        self.all_sprites_list.append(self.rotor)
        self.rotor_list.append(self.rotor)

        #SETUP ENEMY
        for i in range (BAD_GUY_COUNT):

            self.enemy1_sprite = EnemySprite("Bad_Guys/Alien1.png", SPRITE_SCALING_PLAYER)
            self.all_sprites_list.append(self.enemy1_sprite)
            self.enemy1_list.append(self.enemy1_sprite)
        for j in range (BAD_GUY_COUNT):

            self.enemy2_sprite = EnemySprite("Bad_Guys/Alien2.png", SPRITE_SCALING_PLAYER)

            self.all_sprites_list.append(self.enemy2_sprite)
            self.enemy2_list.append(self.enemy2_sprite)


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        if self.current_state == INSTRUCTIONS:
            print("Instructions")
            text1 = arcade.load_texture("Instructions.png")
            scale_text1 = 0.6
            arcade.draw_texture_rectangle(SCREEN_WIDTH //2, SCREEN_HEIGHT//2,
                                        scale_text1 * text1.width, scale_text1 * text1.height, text1, 0)
            self.set_mouse_visible(True)


        elif self.current_state == GAME_RUNNING:
            print("Game Running")
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                          SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
            self.all_sprites_list.draw()
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.YELLOW, 12)
            self.set_mouse_visible(False)
        else:
            print("Game over")
            self.all_sprites_list.draw()
            text2 = arcade.load_texture("GameOver.png")
            scale_text2 = 1
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                          SCREEN_WIDTH, SCREEN_HEIGHT, text2, 0)
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.BLACK, 12)



    def on_mouse_motion(self, x, y, dx, dy):
        # MAKE MOUSE MOVE
        if self.current_state == GAME_RUNNING:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y
            self.rotor.center_x = x
            self.rotor.center_y = y+24

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == INSTRUCTIONS:
            #START GAME
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            #self.setup()
            self.current_state = INSTRUCTIONS

        if self.current_state == GAME_RUNNING:
            # MAKE BULLETS
            if button == arcade.MOUSE_BUTTON_LEFT:
                #RIGHT GUN
                blackbullet = arcade.Sprite("Bullets/Black_Bullet.png",
                                            SPRITE_SCALING_BULLET)
                blackbullet.angle = 0

                blackbullet.change_y = PLAYER_BULLET_SPEED


                blackbullet.center_x = self.player_sprite.center_x+17
                blackbullet.bottom = self.player_sprite.top
                self.all_sprites_list.append(blackbullet)
                self.blackbullet_list.append(blackbullet)
                #MIDDLE GUN
                blackbullet = arcade.Sprite("Bullets/Black_Bullet.png",
                                            SPRITE_SCALING_BULLET)
                blackbullet.angle = 0

                blackbullet.change_y = PLAYER_BULLET_SPEED

                blackbullet.center_x = self.player_sprite.center_x
                blackbullet.bottom = self.player_sprite.top
                self.all_sprites_list.append(blackbullet)
                self.blackbullet_list.append(blackbullet)
                #LEFT GUN
                blackbullet = arcade.Sprite("Bullets/Black_Bullet.png",
                                            SPRITE_SCALING_BULLET)
                blackbullet.angle = 0

                blackbullet.change_y = PLAYER_BULLET_SPEED

                blackbullet.center_x = self.player_sprite.center_x-17
                blackbullet.bottom = self.player_sprite.top
                self.all_sprites_list.append(blackbullet)
                self.blackbullet_list.append(blackbullet)

    def update(self, delta_time):

        if self.current_state == GAME_RUNNING:

            self.player_list.update()
            self.player_sprite.update()
            self.all_sprites_list.update()
            self.blackbullet_list.update()
            self.redbullet_list.update()

            self.enemy2_list.move(0, -2)
            #SHOOT THE BAD GUYS
            for blackbullet in self.blackbullet_list:


                hit1_list = arcade.check_for_collision_with_list(blackbullet, self.enemy1_list)
                hit2_list = arcade.check_for_collision_with_list(blackbullet, self.enemy2_list)

                if len(hit1_list) > 0:
                    blackbullet.kill()
                if len(hit2_list) > 0:
                    blackbullet.kill()


                for enemy1 in hit1_list:
                    enemy1.reset_pos()
                    self.score +=1
                for enemy2 in hit2_list:
                    enemy2.reset_pos()
                    self.score +=2


                if blackbullet.bottom > SCREEN_HEIGHT:
                    blackbullet.kill()
            #BAD GUYS SHOOTS YOU
            for enemy1 in self.enemy1_list:
                if random.randrange(80) == 0:
                    redbullet = arcade.Sprite("Bullets/Red_Bullet.png",
                                          SPRITE_SCALING_PLAYER)
                    redbullet.center_x = enemy1.center_x
                    redbullet.angle = 0
                    redbullet.top = enemy1.bottom
                    redbullet.change_y = -ENEMY_BULLET_SPEED
                    self.all_sprites_list.append(redbullet)
                    self.redbullet_list.append(redbullet)

            for enemy2 in self.enemy2_list:
                if random.randrange(80) == 0:
                    redbullet = arcade.Sprite("Bullets/Red_Bullet.png",
                                          SPRITE_SCALING_PLAYER)
                    redbullet.center_x = enemy2.center_x
                    redbullet.angle = 0
                    redbullet.top = enemy2.bottom
                    redbullet.change_y = -ENEMY_BULLET_SPEED
                    self.all_sprites_list.append(redbullet)
                    self.redbullet_list.append(redbullet)
            for redbullet in self.redbullet_list:
                #JUST INCASE IF REDBULLET GO OFFSCREEN, RED BULLET DISAPPEARS
                if redbullet.top < 0:
                    redbullet.kill()

                shot1_list = arcade.check_for_collision_with_list(redbullet, self.player_list)
                shot2_list = arcade.check_for_collision_with_list(redbullet, self.rotor_list)

                #IF RED BULLET HITS THE PLAYER, DISABLE RED BULLET
                if len(shot1_list) > 0 and len(shot2_list):
                    redbullet.kill()

                #PLAYER IS DEAD
                for player in shot1_list:
                    player.kill()
                for rotor in shot2_list:
                    rotor.kill()

                #IF PLAYER IS DEAD, GAME OVER
                if len(self.player_list) == 0 or len(self.rotor_list) == 0:
                   # print("Game over")
                    self.current_state = GAME_OVER
                    self.set_mouse_visible(True)



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()