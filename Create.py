import random
from Guy import guy

mutation = 1
maxB = 1

def createGen(guys, layers, npl):
    global maxB
    colordiff = int(round(64 / guys, 0))
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
        color = colordiff * dawg + 1
        result.append(guy(guyInput, color))
    return result

def nextGen(inp):
    survivors = inp[:]
    newGen = []
    restock = []
    for x in range(64):
        if len(survivors) > 1:
            parent1 = survivors.pop(random.randint(0, len(survivors) - 1))
            parent2 = survivors.pop(random.randint(0, len(survivors) - 1))
            newGen.append(reproduce(parent1, parent2))
            restock.append(parent1)
            restock.append(parent2)
        else:
            if len(survivors) == 1:
                restock.append(survivors.pop(0))
            survivors = restock[:]
            restock = []
    return newGen

def reproduce(p1, p2):
    global mutation, maxB
    layers = len(p1.brain) + 1 # find number of layers
    npl = [len(p1.brain[0][0][0])]
    for l in p1.brain: # find neurons per layer
        npl.append(len(l))

    guyInput = []
    for lay in range(1, layers):
        prin = []
        for neuron in range(npl[lay]):
            neu = []
            weights = []
            for x in range(npl[lay - 1]):
                if random.randint(0,1) == 1:
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
    if random.randint == 1:
        c = p1.c
    else:
        c = p2.c
    c += random.randint(-1,1)
    c = makeReal(c, 1, 64)

    kid = guy(guyInput, c)
    return kid

def makeReal(num, min, max):
    if num > max:
        num = max
    elif num < min:
        num = min
    return num

