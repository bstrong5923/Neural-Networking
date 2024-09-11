import random

directions = ["N","E","S","W"]
input = directions[random.randint(0,3)]


class A:
    def __init__(self, want):
        if want == input:
            self.v = 1
        else:
            self.v = 0

class B:
    def __init__(self, w, b):
        self.v = w[0]*As[0]+w[1]*As[1]+w[2]*As[2]+w[3]*As[3]+b

As = [
    A("N"), A("E"), A("S"), A("W")
]

neuron = B([1.4,6.3,3.2,0.6], 1.1)
print(input)
print(neuron)