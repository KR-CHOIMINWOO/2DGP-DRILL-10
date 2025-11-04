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
FRAMES_PER_ACTION = 14
FRAME_PER_SECOND = FRAMES_PER_ACTION * ACTIONS_PER_TIME

class Bird:
    image = None

    def __init__(self, x = 400, y = 500, throwin_speed = 15):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.xv = throwin_speed
        self.frame = 0
        self.frame_index = 0
        self.frame_x = 0
        self.frame_y = 0
        self.face_dir = 1

    def draw(self):
        width = 180
        height = 160
        high = 3 * height

        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame_x) * width, high - (self.frame_y + 1) * height, width, height, 0, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame_x) * width, high - (self.frame_y + 1) * height, width, height, 0, 'h', self.x, self.y, 100, 100)

    def update(self):
        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTIONS_PER_TIME * game_framework.frame_time) % 14

        self.frame_index = int(self.frame)
        self.frame_x = self.frame_index % 5
        self.frame_y = self.frame_index // 5

        if self.x >= 1600:
            self.face_dir = -1
            self.xv = -self.xv
        elif self.x <= 0:
            self.face_dir = 1
            self.xv = -self.xv