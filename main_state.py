import random
import game_framework
import title_state
from pico2d import *
from Player import Player
from Enemy import EnemyOne
from Enemy import EnemyTwo
from Enemy import EnemyThree
from Enemy import Boss
from Enemy import MiddleBoss

name = "MainState"

running = None
player = None

class Map:
    def __init__(self):
        self.image = load_image('object/Canvas/Map.png')

    def draw(self):
        self.image.draw(400,375)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            player.handle_event(event)

def enter():
    global map, player, enemyone, enemytwo, enemythree, middleboss, boss
    map = Map()
    player = Player()
    enemyone = EnemyOne()
    enemytwo = EnemyTwo()
    enemythree = EnemyThree()
    boss = Boss()
    middleboss = MiddleBoss()


def exit():
    global map, player, enemyone, enemytwo, enemythree, middleboss,  boss

    del(enemyone)
    del(enemytwo)
    del(enemythree)
    del(player)
    del(map)
    del (middleboss)
    del(boss)



def update():
    player.update()
    enemyone.update()
    enemytwo.update()
    enemythree.update()
    boss.update()
    middleboss.update()

def draw():
    clear_canvas()
    map.draw()
    player.draw()
    enemyone.draw()
    enemytwo.draw()
    enemythree.draw()
    boss.draw()
    middleboss.draw()
    delay(0.04)
    update_canvas()

def main():
    enter()

    running = True;
    while running:
        handle_events()
        update()
        draw()

    exit()

if __name__ == '__main__':
    main()