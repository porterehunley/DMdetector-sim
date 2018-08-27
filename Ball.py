import numpy as np
import Particles as par
import VelocityField as vel

class Ball(object):
    def __init__(self, field):  # field means the vector field object
        self.xPos = 0
        self.zPos = 0
        self.xPositions = []
        self.zPositions = []
        self.position = [self.xPos, 0, self.zPos]
        self.timestep = 5
        self.radius = 50
        self.box = None
        self.t = 0
        self.simtime = 0
        self.field = field
        self.Radons = []
        self.Xvel = None
        self.Zvel = None
        self.diffX = -1
        self.diffZ = -1

    def run(self, Radon):
        self.xPos = Radon.position[0]
        self.zPos = Radon.position[2]
        self.zPositions = []
        self.xPositions = []
        firstRun = True
        self.setPos()
        self.simtime = Radon.partner.time - Radon.time

        self.t = 0
        while (self.t < self.simtime):
            self.radius = 50
            for po in self.field.constructors:
                self.add(po.partner)
            self.cleanse()
            if (len(self.Radons) != 0):
                self.setVelocity()
            else:
                while len(self.Radons) == 0:
                    self.radius = self.radius + 10
                    for po in self.field.constructors:
                        self.add(po.partner)
                    self.cleanse()
                self.setVelocity()

            self.xPos = self.xPos + self.Xvel * self.timestep
            self.zPos = self.zPos + self.Zvel * self.timestep
            self.xPositions.append(self.xPos)
            self.zPositions.append(self.zPos)
            if firstRun:
                Radon.xVel = self.Xvel
                Radon.zVel = self.Zvel
                firstRun = False
            self.t = self.t + self.timestep
        return self.within(Radon.partner)

    def setPos(self):
        self.position = [self.xPos, 0, self.zPos]

    def within(self, Particle):
        if (Particle.position[0] > self.xPos - self.radius and Particle.position[0] < self.xPos + self.radius):
            if (Particle.position[2] > self.zPos - self.radius and Particle.position[2] < self.zPos + self.radius):
                return True
            else:
                return False
        else:
            return False

    def add(self, Radon):
        if (self.within(Radon)):
            self.Radons.append(Radon)

    def cleanse(self):
        if (len(self.Radons) != 0):
            for rn in self.Radons:
                if (self.within(rn) == False):
                    self.Radons.remove(rn)

    def setVelocity(self):
        Xvels = []
        Zvels = []
        for rn in self.Radons:
            Xvels.append(rn.xVel)
            Zvels.append(rn.zVel)

        self.Xvel = sum(Xvels) / len(Xvels)
        self.Zvel = sum(Zvels) / len(Zvels)



