import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *

import random
import numpy as np

HEIGHT = 1024
WIDTH = 1024

class guy:
    def __init__(self):
        self.show = Actor("red")
    def move(self, n, e, s, w):
        NS = 0
        EW = 0
        NESW = 0
        if n > s:
            NS = 1
        if e > w:
            EW = 1
        if NS == 1:
            if EW == 1:



isaac = guy()

def draw():
    screen.clear()
    screen.fill((255,255,255,255))
    isaac.show.draw()

def update():
    print("hi")

pgzrun.go()