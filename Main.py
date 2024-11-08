import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *

from time import sleep
import random
from Create import createGen, nextGen

width = 120
height = 65
WIDTH = 16 * width
HEIGHT = 16 * height

pause = False
mousex = width / 2
mousey = height / 2

guys = createGen(64, 3, [3, 7, 7])

limit = 110 # TOTAL TICKS
s = 250 # TICKS/SEC

t = 0
gen = 1

def scatter(): #Spawn randomly
    for guy in guys:
        guy.x = random.randint(2, width - 2)
        guy.y = random.randint(2, height - 2)
        guy.d = random.randint(0,3)

def center(x, y):
    for guy in guys:
        guy.x = x
        guy.y = y
        guy.d = random.randint(0,3)


def draw():
    global gen
    screen.clear()
    screen.fill((255,255,255,255))
    for guy in guys:
        guy.actor.draw()
        if pause:
            screen.draw.text(str(guy.c), color="black", center=(guy.actor.x, guy.actor.y), fontsize=12, fontname="pixchicago")
    screen.draw.text("Gen " + str(gen), color="black", topleft=(8, 2), fontsize=22, fontname="pixchicago")

def update():
    global t, limit, guys, s, gen
    if t >= limit:
        pops = []
        for g in range(len(guys)):
            if guys[g].x < width / 2:
                pops.insert(0, g)
        for g in pops:
            guys.pop(g)
        guys = nextGen(guys)
        gen += 1
        scatter()
        t = 0
    if not pause:
        for guy in guys:
            guy.act(guy.choose(height, width), height, width)
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
    elif key == key.R:
        scatter()
    elif key == key.E:
        center(mousex, mousey)
def on_mouse_move(pos):
    global mousex, mousey
    mousex = int(pos[0] / 16)
    mousey = int(pos[1] / 16)

scatter()

pgzrun.go()
