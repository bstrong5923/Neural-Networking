import random
from Guy import guy

mutation = 2

def createGen(guys, layers, npl):
    colordiff = int(round(64 / guys, 0))
    result = []
    print(str(layers))
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
                bias = random.randint(0, int(total) * 50) / 100
                denom = round(total + bias, 2)
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
    global mutation
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
                bias = makeBias(p1.brain, lay, neuron, total)
            else:
                bias = makeBias(p2.brain, lay, neuron, total)
            denom = round(total + bias, 2)
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

def makeBias(brain, lay, neuron, total):
    global mutation
    percent = brain[lay - 1][neuron][1] / brain[lay - 1][neuron][2]
    bias = round(total * percent, 2)
    bias += round(random.randint(-3 * mutation, 3 * mutation) / 300, 2)
    bias = makeReal(bias, .01, round((bias + total) * 0.34, 2))
    return bias

def makeReal(num, min, max):
    if num > max:
        num = max
    elif num <= 0:
        num = min
    return num

