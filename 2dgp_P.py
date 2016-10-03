from pico2d import *

open_canvas()

Map = load_image('Map.png')
C = load_image('acacac.png')

x = 0
while (x < 800):
    clear_canvas()
    Map.draw(400,300)
    C.draw(x,80)
    x = x + 2
    update_canvas()
    delay(0.01)

close_canvas()