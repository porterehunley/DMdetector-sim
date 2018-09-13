import numpy as np
import Ball as bll
import Square as sq
import matplotlib.pyplot as plt

#This is the class that holds the vector field
#The vector field uses the ball method here to reconstruct
def plotVectors2D(Arr, xmin, xmax, zmin, zmax): #Takes the array and the dimensions of the space and plots them
    X, Y, U, V = zip(*Arr)
    plt.figure(figsize=(10,10), dpi=80)
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=.2)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([zmin, zmax])
    plt.draw()
    plt.show()

class vectorField(object):  # Draws Vectors from objects
    def __init__(self, Poloniums):  # Poloniums should be a MATCHED LIST of Polonium Objects, ThreeDim is boolean
        self.Pos = Poloniums
        self.vector = []
        self.threeDim = False
        self.temp = []
        self.posDiffX = 0
        self.posDiffY = 0
        self.posDiffZ = 0
        self.vectorArray = []
        self.rn = None
        self.constructors = []
        self.newConstructors = []
        self.others = []
        self.Xmin = 0
        self.Xmax = 0
        self.Zmin = 0
        self.Zmax = 0
        self.boxs = []

    def Filter(self):
        self.constructors = []
        for po in self.Pos:
            self.rn = po.partner
            self.posDiffX = po.position[0] - self.rn.position[0]
            self.posDiffY = po.position[1] - self.rn.position[1]
            self.posDiffZ = po.position[2] - self.rn.position[2]

            posMag = np.sqrt(self.posDiffX ** 2 + self.posDiffY ** 2 + self.posDiffZ ** 2)  # magnitude of vector
            if (po.time - po.partner.time < 50 and posMag < 200):
                self.constructors.append(po)
            else:
                self.others.append(po)


    def reconstruct(self):
        ball = bll.Ball(self)

        for po in self.others:
            if ball.run(po.partner):
                self.newConstructors.append(po)
                self.others.remove(po)
                #xPositions = np.asarray(ball.xPositions)
                #zPositions = np.asarray(ball.zPositions)
                #plt.plot(xPositions,zPositions)
                #plt.axis([-500, 500, 0, -1000])
                #plt.show()

    def vectorize(self, ThreeDim):  # from radon to Polonium
        self.threeDim = ThreeDim
        self.Filter()
        self.setConstructorVelocity()
        for po1 in self.constructors:
            self.temp = []
            self.rn = po1.partner
            if (self.threeDim):  # ignore everything till else, this is broken
                self.posDiffX = po1.position[0] - self.rn.position[0]
                self.posDiffY = po1.position[1] - self.rn.position[1]
                self.posDiffZ = po1.position[2] - self.rn.position[2]
            else:
                self.temp.append(self.rn.position[0])  # radon position is the tail of vector
                self.temp.append(self.rn.position[2])
                self.temp.append(self.rn.xVel)
                self.temp.append(self.rn.zVel)  # uses position unit vecotr and magnitude of velocity vector
                self.vector.append(self.temp)  # puts it into good form for numpy
        if len(self.newConstructors) != 0:
            for po in self.newConstructors:
                self.rn = po.partner
                self.temp = []
                self.temp.append(self.rn.position[0])  # radon position is the tail of vector
                self.temp.append(self.rn.position[2])
                self.temp.append(self.rn.xVel)
                self.temp.append(self.rn.zVel)

                self.vector.append(self.temp)


        self.vectorArray = np.asarray(self.vector)  # puts it into an array that matplotlib can use
        return self.vectorArray  # returns the Array
    def setConstructorVelocity(self):
        for po in self.constructors:
            self.rn = po.partner
            self.posDiffX = po.position[0] - self.rn.position[0]
            self.posDiffZ = po.position[2] - self.rn.position[2]

            posMag = np.sqrt(self.posDiffX ** 2 + self.posDiffZ ** 2)  # magnitude of vector
            unitX = self.posDiffX / posMag
            unitZ = self.posDiffZ / posMag  # direction vector

            velocityX = self.posDiffX / (po.time - self.rn.time)
            velocityZ = self.posDiffZ / (po.time - self.rn.time)
            velMag = np.sqrt(velocityX ** 2 + velocityZ ** 2)  # magnitude of velocity vector

            self.rn.xVel = unitX * velMag
            self.rn.zVel = unitZ * velMag







