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
    def __init__(self, neurons):
        self.show = Actor("arrow")

    def move(self, choices):
        print(options[self.find_max(choices)])

    def find_max(self, choices):
        max = 0
        for x in range(len(choices)):
            if choices[x] > choices[max]:
                max = x
        return max



# def draw():
#     screen.clear()
#     screen.fill((255,255,255,255))
#     isaac.show.draw()
#
# def update():
#     print("hi")
#
# pgzrun.go()