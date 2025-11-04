from pico2d import load_image, get_time, load_font

import game_world
import game_framework
from ball import Ball


# Boy의 Run Speed 계산
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0            # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
Time_PER_ACTION = 0.5
ACTIONS_PER_TIME = 1.0 / Time_PER_ACTION
FRAMES_PER_ACTION = 8
FRAME_PER_SECOND = FRAMES_PER_ACTION * ACTIONS_PER_TIME








class Idle:

    def __init__(self, bird):
        self.bird = bird

    def enter(self, e):
        self.bird.wait_time = get_time()
        self.bird.dir = 0


    def exit(self, e):
        pass

    def do(self):
        self.bird.frame = (self.bird.frame + FRAMES_PER_ACTION * ACTIONS_PER_TIME * game_framework.frame_time) % 8
        if get_time() - self.bird.wait_time > 3:
            self.bird.state_machine.handle_state_event(('TIMEOUT', None))

    def draw(self):
        if self.bird.face_dir == 1: # right
            self.bird.image.clip_draw(int(self.bird.frame) * 100, 300, 100, 100, self.bird.x, self.bird.y)
        else: # face_dir == -1: # left
            self.bird.image.clip_draw(int(self.bird.frame) * 100, 200, 100, 100, self.bird.x, self.bird.y)



class Bird:
    def __init__(self):

        self.item = None

        self.x, self.y = 400, 550
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')

        self.IDLE = Idle(self)



    def update(self):
        pass


    def handle_event(self, event):
        pass


    def draw(self):
        pass

