import random
from pico2d import *

name = "MainState"

running = None
player = None

class Map:
    def __init__(self):
        self.image = load_image('object/Map.png')

    def draw(self):
        self.image.draw(400,375)

class Player:
    image = None
    frameSize = 9

    LEFT, RIGHT, IDLE, UP, DOWN = 0, 1, 2, 3, 4

    global rightmove, leftmove, upmove, downmove

    leftmove = False
    rightmove = False
    upmove = False
    downmove = False


    def __init__(self):
        self.x = 400
        self.y = 90
        self.x1 = 0
        self.y1 = 0
        self.state = self.IDLE
        self.frame = random.randint(0, 1)
        if Player.image == None:
            Player.image = load_image('object/Player.png')

    def update(self):
        global rightmove, leftmove, upmove, downmove

        self.frame = (self.frame + 1) % self.frameSize

        if (rightmove == True):
            self.x += 10
            if(upmove == True):
                self.x += 10
                self.y += 10
            elif(downmove == True):
                self.x += 10
                self.y -= 10
        elif (leftmove == True):
            self.x -= 10
            if (upmove == True):
                self.x -= 10
                self.y += 10
            elif (downmove == True):
                self.x -= 10
                self.y -= 10
        elif (upmove == True):
            self.y += 10
            if (rightmove == True):
                self.y += 10
                self.x += 10
            elif (leftmove == True):
                self.y += 10
                self.x -= 10
        elif (downmove == True):
            self.y -= 10
            if (rightmove == True):
                self.y -= 10
                self.x += 10
            elif (leftmove == True):
                self.y -= 10
                self.x -= 10

        def clamp(minimum, y, maximum):
            return max(minimum, min(y, maximum))

        self.x += self.x1
        self.y += self.y1

        self.x = clamp(50, self.x, 710)
        self.y = clamp(50, self.y, 650)

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        global leftmove, rightmove, upmove, downmove
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            rightmove = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            leftmove = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            upmove = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            downmove = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            rightmove = False
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            leftmove = False
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            upmove = False
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            downmove = False

class Enemy:
    image = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image('object/Enemy.png')

    def draw(self):
        self.image.draw(400, 700)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            runnig = False
        else:
            player.handle_event(event)

def main():

    open_canvas(800,750)

    global player
    global running

    player = Player()
    map = Map()
    enemy = Enemy()
    running = True

    while running:
        handle_events()

        player.update()

        clear_canvas()

        map.draw()
        enemy.draw()
        player.draw()

        update_canvas()

        delay(0.04)

    close_canvas()

if __name__ == '__main__':
    main()