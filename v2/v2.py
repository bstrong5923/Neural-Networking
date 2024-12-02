import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *
from time import sleep
import random

# GUY CLASS

class guy:
    def __init__(self, neurons):
        self.d = 3
        self.actor = Actor("bear")
        self.speed = 1
        self.x = 0
        self.y = 0
        self.hungry = 1


        # DONT TOUCH
        self.brain = neurons
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


# CREATING GENERATIONS

mutation = 1
maxB = 1

def firstGuys(brains):
    global maxPop
    result = []
    for dawg in range(len(brains)):
        result.append(guy(brains[dawg]))
    return result

def reproduce(p1, p2):
    global maxPop
    brain = makeBrain(p1, p2)
    kid = guy(brain)
    return kid

# DONT TOUCH v
def firstBrains(guys, layers, npl):
    global maxB

    result = []
    for dawg in range(guys):
        guyInput = []
        for lay in range(1, layers):
            prin = []
            for neuron in range(npl[lay]):
                neu = []
                weights = []
                for x in range(npl[lay - 1]):
                    add = random.randint(0,800) / 100
                    weights.append(add)
                neu.append(weights)
                total = sum(weights)
                bias = random.randint(0, 100 * maxB) / 1000
                denom = round(total * 1.5, 2)
                neu.append(bias)
                neu.append(denom)
                prin.append(neu)
            guyInput.append(prin)

        result.append(guyInput)
    return result
def newGuys(inp):
    global maxPop
    survivors = inp[:]
    newGen = []
    restock = []
    for x in range(maxPop):
        if len(survivors) <= 1:
            if len(survivors) == 1:
                restock.append(survivors.pop(0))
            survivors = restock[:]
            restock = []
        parent1 = survivors.pop(random.randint(0, len(survivors) - 1))
        parent2 = survivors.pop(random.randint(0, len(survivors) - 1))
        newGen.append(reproduce(parent1, parent2))
        restock.append(parent1)
        restock.append(parent2)

    return newGen
def makeBrain(p1, p2):
    global mutation, maxB
    layers = len(p1.brain) + 1  # find number of layers
    npl = [len(p1.brain[0][0][0])]
    for l in p1.brain:  # find neurons per layer
        npl.append(len(l))

    guyInput = []
    for lay in range(1, layers):
        prin = []
        for neuron in range(npl[lay]):
            neu = []
            weights = []
            for x in range(npl[lay - 1]):
                if random.randint(0, 1) == 1:
                    add = p1.brain[lay - 1][neuron][0][x]
                else:
                    add = p2.brain[lay - 1][neuron][0][x]
                add = round(add + random.randint(-mutation, mutation) / 100, 2)
                add = makeReal(add, .01, 8)
                weights.append(add)
            neu.append(weights)
            total = sum(weights)
            if random.randint(0, 1) == 1:
                bias = p1.brain[lay - 1][neuron][1]
            else:
                bias = p2.brain[lay - 1][neuron][1]
            bias += random.randint(-mutation, mutation) / 1000
            bias = round(makeReal(bias, 0, 0.1 * maxB), 3)
            denom = round(total * (1 + 0.1 * maxB), 2)
            neu.append(bias)
            neu.append(denom)
            prin.append(neu)
        guyInput.append(prin)
    return guyInput



def getInput(g):
    global apples
    best = 100
    besta = 0
    for a in range(len(apples)):
        apple = apples[a]
        diff = abs(apple.x - g.actor.x) + abs(apple.y - g.actor.y)
        if diff < best:
            best = diff
            besta = a
    besta = apples[besta]
    xdiff = besta.x / 16 - g.x
    xdiff = 0.5 + (xdiff / w)
    ydiff = besta.y / 16 - g.y
    ydiff = 0.5 + (ydiff / h)
    return [g.x / w, g.y / h, g.d / 3, xdiff, ydiff]

def act(g, x):
    if x <= 3:
        turn(g, x)
    else:
        move(g, x - 4)
    updateGuy(g)

def updateGuy(g):
    g.actor.x = g.x * 16
    g.actor.y = g.y * 16
    g.actor.angle = g.d * -90
    boundary(g, 2)

def boundary(g, indent):
    if g.y > h - indent:
        g.y = h - indent
    elif g.y < indent:
        g.y = indent
    elif g.x > w - indent:
        g.x = w - indent
    elif g.x < indent:
        g.x = indent

def turn(g, val):
    g.d += val
    if g.d > 3:
        g.d -= 4


def move(g, val):
    r = g.d + val
    if r > 3:
        r -= 4
    if r == 0:
        g.y += g.speed
    elif r == 1:
        g.x += g.speed
    elif r == 2:
        g.y -= g.speed
    else:
        g.x -= g.speed

def visual():
    global guys
    result = []
    for guy in guys:
        result.append(guy.actor)
    for apple in apples:
        result.append(apple)
    return result

def restart():
    global guys
    pops = []
    for g in range(len(guys)):
        if guys[g].hungry == 1:
            pops.insert(0, g)
    for g in pops:
        guys.pop(g)
    guys = newGuys(guys)
    scatter()
    makeApples()

def run():
    for guy in guys:
        act(guy, findMax(guy.choose(getInput(guy))) + 1)
        for a in range(len(apples)):
            apple = apples[a]
            if guy.actor.collidepoint(apple.x, apple.y):
                guy.hungry = 0
                apples.pop(a)
                break


def start():
    global guys, fc, fn, h, w, limit, s, maxPop

    maxPop = 16

    guys = firstGuys(firstBrains(maxPop, 2, [5, 7]))

    fc = "black"
    fn = "pixchicago"

    w = 20
    h = 20

    limit = 50  # TOTAL TICKS
    s = 250  # TICKS/SEC

    initial()
    scatter()
    makeApples()

#Spawn randomly
def scatter():
    global guys
    for guy in guys:
        guy.x = random.randint(2, w - 2)
        guy.y = random.randint(2, h - 2)
        guy.d = random.randint(0,3)

#spawn apples
def makeApples():
    global apples
    apples = []
    for x in range(maxPop * 3):
        apples.append(Actor("apple"))
    for apple in apples:
        apple.x = random.randint(2, w - 2) * 16
        apple.y = random.randint(2, h - 2) * 16



# KEY CONTROLS
def on_key_down(key):
    global pause
    if key == key.SPACE:
        pause = True
def on_key_up(key):
    global pause, s
    if key == key.SPACE:
        pause = False
    elif key == key.UP:
        s = round(s * 1.25, 0)
    elif key == key.DOWN:
        s = round(s * 0.8, 0)



# v v v v v v v v v v v
# v DONT TOUCH BELOW! v
# v v v v v v v v v v v

def findMax(choices):
    max = 0
    for x in range(len(choices)):
        if choices[x] > choices[max]:
            max = x
    return max
def makeReal(num, min, max):
    if num > max:
        num = max
    elif num < min:
        num = min
    return num

def initial():
    global pause, t, gen, HEIGHT, height, WIDTH, width
    pause = False
    t = 0
    gen = 1
    HEIGHT = h * 16
    WIDTH = w * 16
def draw():
    global gen
    screen.clear()
    screen.fill((255,255,255,255)) # BACKGROUND COLOR
    for thing in visual():
        thing.draw()
    screen.draw.text("Gen " + str(gen), color=fc, topleft=(8, 2), fontsize=22, fontname=fn)
def update():
    global t, limit, s, gen

    # Next Generation
    if t >= limit:
        restart()
        gen += 1
        t = 0

    if not pause:
        run()
        sleep(1 / s)
        t += 1


start()
pgzrun.go()