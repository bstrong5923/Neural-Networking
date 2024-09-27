import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *

import random
import numpy as np

HEIGHT = 1024
WIDTH = 1024

options = ["Stay Still", "Turn 90°", "Turn 180°", "Turn 270°", "Go Forward", "Go Right", "Go Backward", "Go Left"]

class guy:
    def __init__(self):
        self.show = Actor("arrow")
    def move(self, choices):
        done = 0
        for x in range(len(choices)):
            if done == 0:
                me = 1
                for y in range(x + 1, len(choices)):
                    if choices[x] < choices[y]:
                        me = 0
                if me == 1:
                    choice = options[x]
                    done = 1
        print(choice)

isaac = guy()

vals = [random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000)]
print(options)
print(vals)
isaac.move(vals)

def draw():
    screen.clear()
    screen.fill((255,255,255,255))
    isaac.show.draw()

def update():
    print("hi")

pgzrun.go()