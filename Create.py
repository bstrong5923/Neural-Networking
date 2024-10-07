import random

guys = int(input("# of guys: "))
layers = int(input("Number of layers: "))
npl = []
for x in range(layers):
    npl.append(int(input("Neurons in layer " + str(x + 1) + ": ")))
for guy in range(guys):
    prin = ""
    for lay in range(1, layers):
        if lay != 1:
            prin += "]], "
        prin += "[["
        for neuron in range(npl[lay]):
            if neuron != 0:
                prin += "], ["
            weights = []
            for x in range(npl[lay - 1]):
                if x != 0:
                    prin += ", "
                add = random.randint(0,30) / 10
                weights.append(add)
                prin += str(add)
            bias = random.randint(0, int(npl[lay - 1] / 3))
            denom = sum(weights) + bias
    prin += "]]"

    print("guy" + str(guy + 1) + " = guy(" + prin + ")")
