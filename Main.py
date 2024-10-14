import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *

from time import sleep
import random
import Gens
from Guy import HEIGHT, WIDTH
from Create import createGen

options = ["Turn 90°", "Turn 180°", "Turn 270°", "Go Forward", "Go Right", "Go Backward", "Go Left"]

pause = False

# guys = Gens.gen2 #  <----------------------------- WHAT GEN OF GUYS?

guys = createGen(16, 3, [3, 5, 7])

for guy in guys: #Spawn randomly
    guy.actor.x = random.randint(20, WIDTH - 20)
    guy.actor.y = random.randint(20, HEIGHT - 20)
    guy.d = random.randint(0,3)

def draw():
    screen.clear()
    screen.fill((255,255,255,255))
    for guy in guys:
        guy.actor.draw()
        if pause:
            screen.draw.text(str(guy.c), color="black", center=(guy.actor.x, guy.actor.y), fontsize=36)

def update():
    if not pause:
        for guy in guys:
            guy.act(guy.choose())
            guy.actor.angle = guy.d * -90
        sleep(0.1)

def on_key_down(key):
    global pause
    if key == key.SPACE:
        pause = True
def on_key_up(key):
    global pause
    if key == key.SPACE:
        pause = False

pgzrun.go()