from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.03)  # 1 pixel 3 cm
RUN_SPEED_KMPH = 20.0            # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

Time_PER_ACTION = 0.5
ACTIONS_PER_TIME = 1.0 / Time_PER_ACTION
FRAMES_PER_ACTION = 8
FRAME_PER_SECOND = FRAMES_PER_ACTION * ACTIONS_PER_TIME

class Bird:
    image = None

    def __init__(self, x = 400, y = 500, throwin_speed = 15):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.xv = throwin_speed
        self.frame = 0
        self.face_dir = 1

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw((int(self.frame) % 8) * 100, 0, 100, 100, 0, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw((int(self.frame) % 8) * 100, 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)

    def update(self):
        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER

        if self.x >= 1600:
            self.face_dir = -1
            self.xv = -self.xv
        elif self.x <= 0:
            self.face_dir = 1
            self.xv = -self.xv