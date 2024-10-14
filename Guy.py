from pgzhelper import *

WIDTH = 1520
HEIGHT = 960

class guy:
    def __init__(self, neurons, color):
        self.d = 3
        self.actor = Actor(str(color))
        self.speed = 5
        self.brain = neurons
        self.c = color

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
        if self.actor.y > HEIGHT:
            self.actor.y = HEIGHT
        elif self.actor.y < 0:
            self.actor.y = 0
        elif self.actor.x > WIDTH:
            self.actor.x = WIDTH
        elif self.actor.x < 0:
            self.actor.x = 0

    def findMax(self, choices):
        max = 0
        for x in range(len(choices)):
            if choices[x] > choices[max]:
                max = x
        return max

    def choose(self):
        output = [self.actor.x / WIDTH, self.actor.y / HEIGHT, self.d / 3]
        for lay in range(len(self.brain)):
            input = output[:]
            output = []
            for neuron in self.brain[lay]:
                output.append(self.evalNeuron(input, neuron))
        return output

    def evalNeuron(self, input, values):
        val = 0
        for x in range(len(input)):
            val += input[x] * values[0][x] #previous neuron times weight
        val += values[1] #bias
        val = val / values[2] #denom
        return val
    

    def turn(self, val):
        self.d += val
        if self.d > 3:
            self.d -= 4
    def move(self, val):
        r = self.d + val
        if r > 3:
            r -= 4
        if r == 0:
            self.actor.y += self.speed
        elif r == 1:
            self.actor.x += self.speed
        elif r == 2:
            self.actor.y -= self.speed
        else:
            self.actor.x -= self.speed


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