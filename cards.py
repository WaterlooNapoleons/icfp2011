#!/usr/bin/env python

proponent = 0
opponent = ((proponent + 1) % 2)

class Slot:
    def __repr__(self):
        return "{%d, %s}" % (self.v, self.f)
    def __init__(self):
        self.f = "I"
        self.v = 10000

class Error:
    pass

y = []
for x in xrange(256):
    y += [Slot()]
slots = [y, y]

def isValidSlot(i):
    if (not type(i) is int):
        return I
    return i >= 0 and i <= 255

def isSlotDead(player, i):
    return slots[player][i] == 0 or slots[player][i] == -1

############################ CARDS ############################
def I(x):
    return x

def succ(n):
    if (not type(n) is int):
        return I
    if (n < 65535):
        return n+1
    else:
        return 65535

def dbl(n):
    if (not type(n) is int):
        return I
    if (n < 32768):
        return n*2
    else:
        return 65535

def get(i):
    if ((not isValidSlot(i)) or (isSlotDead(proponent, i))):
        return I
    return slots[proponent][i]

def put(x):
    return I

def S(f):
    return (lambda g: (lambda x: (lambda h, y: h(y))(f(x), g(x))))

def K(x):
    return (lambda y: x)

def inc(i):
    if (not type(n) is int):
        return I
    v = slots[proponent][i].v
    if (v > 0 and v < 65535):
        slots[proponent][i].v += 1
    else:
        pass

def dec(i):
    if (not type(n) is int):
        return I
    v = slots[opponent][255].v
    if (v > 0):
        slots[opponent][255].v -= 1
    else:
        pass

def attack(i):
    return (lambda j: (lambda n: processAttack(i, j, n)))

def processAttack(i, j, n):
    if ((not type(n) is int) or (not isValidSlot(i)) or (n > slots[proponent][i].v)):
        return I
    slots[proponent][i].v -= n
    if (isSlotDead(opponent, 255-j)):
        pass
    else:
        if (not isValidSlot(j)):
            return I
        slots[opponent][255-j].v -= min(slots[opponent][255-j].v, int(n*9/10))




def main():
    print slots
