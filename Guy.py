from pgzhelper import *
import Game

class guy:
    def __init__(self, neurons, color):
        self.d = 3
        self.actor = Actor(str(color))
        self.speed = 1
        self.brain = neurons
        self.c = color
        self.x = 0
        self.y = 0

    def act(self, choices):
        Game.act(self, self.findMax(choices) + 1)


    def findMax(self, choices):
        max = 0
        for x in range(len(choices)):
            if choices[x] > choices[max]:
                max = x
        return max


    def choose(self, invals):
        output = invals
        for lay in range(len(self.brain)):
            input = output[:]
            output = []
            for neuron in self.brain[lay]:
                output.append(self.evalNeuron(input, neuron))
        return output


    def evalNeuron(self, input, values):
        val = 0
        total = 0
        for x in range(len(input)):
            total += values[0][x]
            val += input[x] * values[0][x]  # previous neuron times weight
        val += values[1] * total  # bias
        val = val / values[2]  # denom
        return val
