import random
import Create

guys = Create.firstGen(64, 3, [3, 7, 7])

fontColor = "black"
fontName = "pixchicago"

w = 120
h = 65

limit = 110 # TOTAL TICKS
s = 250 # TICKS/SEC

def getInput(g):
    return [g.x / w, g.y / h, g.d / 3]

def act(g, x):
    if x <= 3:
        turn(g, x)
    else:
        move(g, x - 4)
    update(g)

def update(g):
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


def start():
    scatter()

def scatter(): #Spawn randomly
    global guys
    for guy in guys:
        guy.x = random.randint(2, w - 2)
        guy.y = random.randint(2, h - 2)
        guy.d = random.randint(0,3)

def visual():
    global guys
    result = []
    for guy in guys:
        result.append(guy.actor)
    return result

def restart():
    global guys
    pops = []
    for g in range(len(guys)):
        if guys[g].x < w / 2:
            pops.insert(0, g)
    for g in pops:
        guys.pop(g)
    guys = Create.nextGen(guys)
    scatter()

def run():
    for guy in guys:
        guy.act(guy.choose(getInput(guy)))