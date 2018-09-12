import math as np
#Polonium and Radon classes form the backbone of all the functions in the simulation
#All classes run with Poloniums and Radons as their inputs
#Only difference between the two classes are the types
#If I could do this differently, i would have the classes inherit from a super
#class of type 'Particle'
class Polonium(object):
    def __init__(self, time, position):
        self.matched = False
        self.time = time
        self.position = position
        self.radius = np.sqrt(position[0] ** 2 + position[1] ** 2)
        self.partner = None
        self.OG = None
        self.type = "Po"
        self.bin = None
        self.timediff = -1
        self.box = -1

    def tmatch(self, Radon):
        self.OG = Radon


class Radon(object):
    def __init__(self, time, position):
        self.matched = False
        self.time = time
        self.position = position
        self.radius = np.sqrt(position[0] ** 2 + position[1] ** 2)
        self.velocity = []
        self.xVel = None
        self.zVel = None
        self.partner = None
        self.OG = None
        self.type = "Rn"
        self.bin = None
        self.box = -1

    def tmatch(self, Polonium):
        self.OG = Polonium
