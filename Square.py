class Square(object):
    def __init__(self, LTcorner, length):  # Lcorner is its top left corner, (x,z)
        self.LTcorner = LTcorner
        self.RTcorner = [self.LTcorner[0] + length, self.LTcorner[1]]
        self.LBcorner = [self.LTcorner[0], self.LTcorner[1] - length]
        self.RBcorner = [self.LTcorner[0] + length, self.LTcorner[1] - length]
        self.velocity = []
        self.Xvels = []
        self.Zvels = []
        self.Xavg = 0
        self.Zavg = 0
        self.vectors = []
        self.belly = []
        self.adjRight = -1
        self.adjLeft = -1

    def eat(self, Radon):
        if (self.within(Radon)):
            self.belly.append(Radon)
            self.vectors.append(Radon.velocity)
            self.Xvels.append(Radon.velocity[0])
            self.Zvels.append(Radon.velocity[1])
            Radon.box = self

    def digest(self):
        if (len(self.Xvels) == 0):
            self.Xavg = 0
            self.Zavg = 0
        else:
            self.Xavg = sum(self.Xvels) / len(self.Xvels)
            self.Zavg = sum(self.Zvels) / len(self.Zvels)
            self.velocity = [self.Xavg, self.Zavg]

    def within(self, Radon):
        if (Radon.position[0] < self.RTcorner[0] and Radon.position[0] >= self.LTcorner[0] and Radon.position[2] >
                self.LBcorner[1] and Radon.position[2] < self.LTcorner[1]):

            return True
        else:
            return False