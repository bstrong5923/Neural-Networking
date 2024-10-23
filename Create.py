import random
from Guy import guy

def printGen():
    guys = int(input("# of guys: "))
    colordiff = int(round(64 / guys, 0))
    layers = int(input("Number of layers: "))
    npl = []
    for x in range(layers):
        npl.append(int(input("Neurons in layer " + str(x + 1) + ": ")))
    prin = "guys = [ #" + str(layers - 2) + " inner layer(s), neurons per layer: "
    for a in range(len(npl) - 2):
        if a != 0:
            prin += ", "
        prin += str(npl[a + 1])
    print(prin)
    for guy in range(guys):
        prin = "["
        for lay in range(1, layers):
            if lay != 1:
                prin += "]], "
            prin += "[[["
            for neuron in range(npl[lay]):
                if neuron != 0:
                    prin += "], [["
                weights = []
                for x in range(npl[lay - 1]):
                    if x != 0:
                        prin += ", "
                    add = random.randint(0,400) / 100
                    weights.append(add)
                    prin += str(add)
                bias = random.randint(0, int(npl[lay - 1] / 3))
                denom = round(sum(weights) + bias, 2)
                prin += "], " + str(bias) + ", " + str(denom)
        prin += "]]]"
        color = colordiff * guy + 1
        if guy != guys - 1:
            print("\tguy(" + prin + ", " + str(color) + "), ")
        else:
            print("\tguy(" + prin + ", " + str(color) + ")")

    print("]")


def createGen(guys, layers, npl):
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
                bias = random.randint(0, int(npl[lay - 1] / 3))
                denom = round(sum(weights) + bias, 2)
                neu.append(bias)
                neu.append(denom)
                prin.append(neu)
            guyInput.append(prin)
        color = colordiff * dawg + 1
        result.append(guy(guyInput, color))
    return result

def nextGen(survivors):
    restock = []
    for x in range(64 - len(survivors)):
        if len(survivors) > 1:
            parent1 = survivors.pop(random.randint(0, len(survivors) - 1))
            parent2 = survivors.pop(random.randint(0, len(survivors) - 1))
            reproduce(parent1, parent2)
            restock.append(parent1)
            restock.append(parent2)
        else:
            if len(survivors) == 1:
                restock.append(survivors.pop(0))
            survivors = restock[:]
            restock = []

def reproduce(p1, p2):
    print(str(p1) + " + " + str(p2))

surviv = [12,45,23,86,3,48,65,73,43,4,5,58,54,2,545,6,24,57,0,83,456,83,53,90,60,56,18,38,28,26,346,856,164,173,376]
print(len(surviv))
nextGen(surviv)