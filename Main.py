import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *

from time import sleep
import Game

fc = Game.fontColor
fn = Game.fontName

WIDTH = 16 * Game.w
HEIGHT = 16 * Game.h

pause = False

limit = Game.limit
s = Game.s

t = 0
gen = 1

def draw():
    global gen
    screen.clear()
    screen.fill((255,255,255,255))
    for thing in Game.visual():
        thing.draw()
    screen.draw.text("Gen " + str(gen), color=fc, topleft=(8, 2), fontsize=22, fontname=fn)

def update():
    global t, limit, s, gen

    # Next Generation
    if t >= limit:
        Game.restart()
        gen += 1
        t = 0

    if not pause:
        Game.run()
        sleep(1 / s)
        t += 1


def on_key_down(key):
    global pause
    if key == key.SPACE:
        pause = True
def on_key_up(key):
    global pause
    if key == key.SPACE:
        pause = False

Game.start()

pgzrun.go()
