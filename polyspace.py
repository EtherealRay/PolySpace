import arcade
import random

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BULLET_SPEED = 5

class Asteroid(arcade.Sprite):

    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 20,SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)
        PolySpaceGame.score -= 1

    def update(self):

        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()
            
class Bullet(arcade.Sprite):
    def update(self):
        self.center_y += BULLET_SPEED
        
class PolySpaceGame(arcade.Window):
    

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.all_sprites_list = arcade.SpriteList()
        self.aster_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
                
        #BG Attribute
        self.bg = arcade.Sprite("images/bg.png")
        self.all_sprites_list.append(self.bg)
        self.bg.center_x = SCREEN_WIDTH/2
        self.bg.center_y = SCREEN_HEIGHT/2

        #Player Attribute
        PolySpaceGame.score = 0
        self.health = 20
        self.player_sprite = arcade.Sprite("images/ship.png", SPRITE_SCALING/3)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.all_sprites_list.append(self.player_sprite)
        
        #Sound
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.ogg")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.ogg")
        
        for i in range(20):
            aster = Asteroid("images/enemy.png", SPRITE_SCALING / random.randrange(3,7))
            aster.center_x = random.randrange(SCREEN_WIDTH)
            aster.center_y = random.randrange(SCREEN_HEIGHT)
            self.all_sprites_list.append(aster)
            self.aster_list.append(aster)
         



    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        output = "SCORE: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)
        output = "HEALTH: {}".format(self.health)
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 16)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.sound.play_sound(self.gun_sound)
        PolySpaceGame.score -= 1
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        self.all_sprites_list.append(bullet)
        self.bullet_list.append(bullet)
        
    def animate(self, delta_time):
        self.all_sprites_list.update()
        hit_list2 = arcade.check_for_collision_with_list(self.player_sprite,self.aster_list)
        
        for aster in hit_list2:
            aster.reset_pos()
            self.health -= 1
        

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet,self.aster_list)
            if len(hit_list) > 0:
                bullet.kill()
                
            for aster in hit_list:
                aster.update()
                aster.reset_pos()
                PolySpaceGame.score += 2
                arcade.sound.play_sound(self.hit_sound)

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()
        

        
 
 
def main():
    PolySpaceGame()
    arcade.run()


if __name__ == "__main__":
    main()

