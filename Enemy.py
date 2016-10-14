from pico2d import *
import random

__author__ = 'user'

class EnemyOne:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(80, 750), random.randint(1000, 1100)
        self.frame = 0
        self.speed = random.randint(5, 6)

    def update(self):
        if (self.y < 0):
            self.y = 750
            self.x = random.randint(30, 770)
        self.y -= self.speed

        if EnemyOne.image == None:
            EnemyOne.image = load_image('object/Enemy/Enemy1.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class EnemyTwo:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(80, 750), random.randint(1000, 1100)
        self.frame = 0
        self.speed = random.randint(5, 6)

    def update(self):
        if (self.y < 0):
            self.y = 750
            self.x = random.randint(30, 770)
        self.y -= self.speed

        if EnemyTwo.image == None:
            EnemyTwo.image = load_image('object/Enemy/Enemy2.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class EnemyThree:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(80, 750), random.randint(1000, 1100)
        self.frame = 0
        self.speed = random.randint(5, 6)

    def update(self):
        if (self.y < 0):
            self.y = 750
            self.x = random.randint(30, 770)
        self.y -= self.speed

        if EnemyThree.image == None:
            EnemyThree.image = load_image('object/Enemy/Enemy3.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class MiddleBoss:
    image = None

    DOWN_IDLE = 0
    def __init__(self):
        self.x, self.y = 200, 550
        self.frame = random.randint(0,1)

        self.state  =  self.DOWN_IDLE
        if MiddleBoss.image == None:
            MiddleBoss.image = load_image('object/Enemy/MiddleBoss.png')

    def update(self):
        if self.state == self.DOWN_IDLE:
            self.frame = (self.frame + 1) % 8

    def draw(self):
             self.image.clip_draw(self.frame * 320, 0, 320, 390, self.x, self.y)

class Boss:
    image = None

    DOWN_IDLE = 0
    def __init__(self):
        self.x, self.y = 600, 580
        self.frame = random.randint(0,1)

        self.state  =  self.DOWN_IDLE
        if Boss.image == None:
            Boss.image = load_image('object/Enemy/Boss.png')

    def update(self):
        if self.state == self.DOWN_IDLE:
            self.frame = (self.frame + 1) % 8

    def draw(self):
             self.image.clip_draw(self.frame * 420, 0, 420, 300, self.x, self.y)