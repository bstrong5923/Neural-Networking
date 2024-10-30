from pgzhelper import *

width = 120
height = 65

WIDTH = 16 * width
HEIGHT = 16 * height


class guy:
    def __init__(self, neurons, color):
        self.d = 3
        self.actor = Actor(str(color))
        self.speed = 1
        self.brain = neurons
        self.c = color
        self.x = 0
        self.y = 0
        self.lastx = 0
        self.lasty = 0

    def act(self, choices):
        x = self.findMax(choices) + 1
        if x <= 3:
            self.turn(x)
        else:
            self.move(x - 4)
        self.update()
        self.boundary(2)

    def update(self):
        self.lastx = self.actor.x
        self.lasty = self.actor.y
        self.actor.x = self.x * 16
        self.actor.y = self.y * 16
        self.actor.angle = self.d * -90


    def boundary(self, indent):
        if self.y > height - indent:
            self.y = height - indent
        elif self.y < indent:
            self.y = indent
        elif self.x > width - indent:
            self.x = width - indent
        elif self.x < indent:
            self.x = indent


    def findMax(self, choices):
        max = 0
        for x in range(len(choices)):
            if choices[x] > choices[max]:
                max = x
        return max


    def choose(self):
        output = [self.x / width, self.y / height, self.d / 3]
        for lay in range(len(self.brain)):
            input = output[:]
            output = []
            for neuron in self.brain[lay]:
                output.append(self.evalNeuron(input, neuron))
        return output


    def evalNeuron(self, input, values):
        val = 0
        for x in range(len(input)):
            val += input[x] * values[0][x]  # previous neuron times weight
        val += values[1]  # bias
        val = val / values[2]  # denom
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
            self.y += self.speed
        elif r == 1:
            self.x += self.speed
        elif r == 2:
            self.y -= self.speed
        else:
            self.x -= self.speed
