import random

guys = int(input("# of guys: "))
layers = int(input("Number of layers: "))
npl = []
for x in range(layers):
    npl.append(int(input("Neurons in layer " + str(x + 1) + ": ")))
for guy in range(guys):
    prin = ""
    for lay in range(1, layers):
        for neuron in range(npl[lay]):
            weights = []
            for x in range(npl[lay - 1]):
                weights.append(random.randint(0,30) / 10)
            bias = random.randint(0, int(npl[lay - 1] / 3))
            denom = sum(weights) + bias
            ", ".join(weights)
            prin += str([weights, bias, denom])

    print("guy" + str(guy + 1) + " = guy(" + prin + ")")
