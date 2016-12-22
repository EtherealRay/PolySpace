import arcade
import random

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BULLET_SPEED = 5

class MyAppWindow(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.all_sprites_list = arcade.SpriteList()

        self.score = 0
        self.player_sprite = arcade.Sprite("images/ship.png", SPRITE_SCALING/2)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.all_sprites_list.append(self.player_sprite)




        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        self.all_sprites_list.draw()

        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
 
 
def main():
    MyAppWindow()
    arcade.run()


if __name__ == "__main__":
    main()

