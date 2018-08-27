class Bin(object): #Needs updating
    def __init__(self, time1, time2):
        self.max = time2
        self.min = time1
        self.bellyRn = []
        self.bellyPo = []
        self.height = 0
        self.midpoint = (time1 + time2) / 2
        self.chi2 = 0
        self.fx = Binned_Func(self.midpoint)
        self.type = "Bin"
        self.adjRight = None
        self.adjLeft = None

    def eat(self, Polonium, ):
        if Polonium.matched == True:
            if (self.max > (Polonium.time - Polonium.partner.time) >= self.min):
                self.bellyRn.append(Polonium.partner)
                self.bellyPo.append(Polonium)
                self.height = len(self.bellyPo)
                self.chi2 = Least_Squares_One_Bin(self.fx, self.height)
                Polonium.bin = self
                Polonium.partner.bin = self

    def vomit(self, Particle):
        if (Particle.type == "Po"):
            self.bellyPo.remove(Particle)
            self.height = len(self.bellyPo)
            self.chi2 = Least_Squares_One_Bin(self.fx, self.height)
            Particle.bin = None
        elif (Particle.type == "Rn"):
            self.bellyRn.remove(Particle)
            Particle.bin = None

    def chi2Test(self, integer):
        return Least_Squares_One_Bin(self.fx, self.height + integer)
