import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *
from time import sleep

import random
import numpy as np

HEIGHT = 1024
WIDTH = 1024

options = ["Turn 90°", "Turn 180°", "Turn 270°", "Go Forward", "Go Right", "Go Backward", "Go Left"]

class Guy:
    def __init__(self, neurons):
        self.d = 3
        self.show = Actor("arrow")
        self.speed = 5

    def act(self, choices):
        x = self.findMax(choices) + 1
        if x == 1:
            self.op1()
        elif x == 2:
            self.op2()
        elif x == 3:
            self.op3()
        elif x == 4:
            self.op4()
        elif x == 5:
            self.op5()
        elif x == 6:
            self.op6()
        elif x == 7:
            self.op7()
        self.boundary()

    def boundary(self):
        if self.show.y > 1024:
            self.show.y = 1024
        elif self.show.y < 0:
            self.show.y = 0
        elif self.show.x > 1024:
            self.show.x = 1024
        elif self.show.x < 0:
            self.show.x = 0

    def findMax(self, choices):
        max = 0
        for x in range(len(choices)):
            if choices[x] > choices[max]:
                max = x
        return max

    def choose(self):
        input = [self.show.x / 1024, self.show.y / 1024, self.d / 3]


    def turn(self, val):
        self.d += val
        if self.d > 3:
            self.d -= 4
    def move(self, val):
        r = self.d + val
        if r > 3:
            r -= 4
        if r == 0:
            self.show.y += self.speed
        elif r == 1:
            self.show.x += self.speed
        elif r == 2:
            self.show.y -= self.speed
        else:
            self.show.x -= self.speed


    def op1(self):
        self.turn(1)
    def op2(self):
        self.turn(2)
    def op3(self):
        self.turn(3)
    def op4(self):
        self.move(0)
    def op5(self):
        self.move(1)
    def op6(self):
        self.move(2)
    def op7(self):
        self.move(3)

guys = [
	Guy([[[2.1, 1.6, 2.3, 2.2], [0.8, 0.3, 1.6, 2.1], [2.3, 0.1, 1.7, 1.6], [1.5, 2.4, 1.5, 2.3], [0.1, 1.0, 0.7, 2.9], [2.0, 0.9, 3.0, 0.5]], [[1.6, 2.1, 0.6, 0.0, 0.1, 1.7], [0.9, 2.4, 2.8, 3.0, 1.9, 2.2], [1.3, 1.9, 0.0, 1.7, 0.5, 2.3], [0.4, 1.7, 2.7, 2.6, 2.9, 0.0]]]),
	Guy([[[1.6, 2.4, 1.6, 0.6], [2.9, 0.5, 1.2, 0.1], [3.0, 1.2, 1.5, 2.2], [0.8, 2.5, 0.7, 1.6], [2.4, 0.5, 0.3, 2.2], [1.0, 0.4, 1.5, 1.3]], [[1.9, 0.7, 2.3, 0.5, 0.8, 2.7], [0.0, 0.6, 2.2, 0.5, 2.6, 1.9], [0.8, 0.8, 1.7, 2.5, 1.6, 2.2], [2.0, 1.0, 0.5, 1.2, 0.6, 2.8]]]),
	Guy([[[0.0, 0.9, 2.2, 1.4], [1.8, 2.3, 2.7, 0.1], [1.4, 2.4, 2.9, 1.8], [1.7, 1.9, 2.4, 0.6], [2.4, 2.1, 0.9, 0.7], [0.3, 1.1, 2.1, 0.3]], [[0.3, 2.3, 0.5, 1.9, 1.7, 0.7], [2.5, 2.3, 1.8, 1.7, 1.3, 1.6], [1.4, 1.3, 1.6, 0.3, 1.3, 0.9], [1.2, 1.7, 2.0, 2.6, 0.7, 0.8]]])
]

for guy in guys:
    guy.show.x = random.randint(20,1004)
    guy.show.y = random.randint(20, 1004)

def draw():
    screen.clear()
    screen.fill((255,255,255,255))
    for guy in guys:
        guy.show.draw()

def update():
    for guy in guys:
        guy.act([random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000)])
        guy.show.angle = guy.d * -90
    sleep(0.5)

pgzrun.go()