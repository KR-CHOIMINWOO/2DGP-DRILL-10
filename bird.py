from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.03)  # 1 pixel 3 cm

class Bird:
    image = None

    def __init__(self, x = 400, y = 500, throwin_speed = 15):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.xv = throwin_speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER

        if self.y < 60:
            game_world.remove_object(self)