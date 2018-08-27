import random
import numpy as np
import Particles as par
class CircularDetector(object):  # Requires Poloniums, Radons, Match Functions, Random,and Numpy
    def __init__(self, decays):
        self.N_Decays = decays
        self.x_max = 500
        self.y_max = 500
        self.z_max = 1000
        self.sim_time = self.N_Decays * 30
        self.Time_Step = .125
        self.Polist = []
        self.Rnlist = []
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        self.delta_t = 0

    def simulate(self):
        Half_Life = 183  # s, Half-life of Polonium
        K = np.log(2) / Half_Life  # Decay constant for Polonium
        a = 0  # a is used to iterate

        while a < self.N_Decays:
            # print(a)

            # Radon Properties
            t1 = random.randrange(30 * self.N_Decays / .125) * .125  # Radon Decay Time (s)

            self.x1 = random.randrange(self.x_max)  # radon x position
            x_sign = random.randrange(0, 2)
            if x_sign == 0:
                self.x1 = -self.x1
            self.y1 = random.randrange(self.y_max)  # radon y position
            y_sign = random.randrange(0, 2)
            if y_sign == 0:
                self.y1 = -self.y1
            self.z1 = -random.randrange(self.z_max)  # radon z position

            s1 = [self.x1, self.y1, self.z1]

            rn = par.Radon(t1, s1)

            if rn.radius > self.x_max:
                continue

            # finding delta t
            self.delta_t = 0
            decayed = False
            while decayed == False:
                chance = random.randrange(1000000)  # Chance of Polonium Decay
                if chance < 472:
                    decayed = True
                self.delta_t = self.delta_t + self.Time_Step

                t2 = t1 + self.delta_t  # polonium decay time (s)

                x_current = self.x1
                y_current = self.y1
                z_current = self.z1

                # Determining velocity based on quadrant
                self.sim_time = 0
            while self.sim_time < self.delta_t:

                # velocity based off of angle
                radius = np.sqrt((z_current + 500) ** 2 + x_current ** 2)
                scale = .01

                x_velocity = scale * radius * ((z_current + 500) / np.sqrt((z_current + 500) ** 2 + x_current ** 2))
                z_velocity = scale * radius * ((-x_current) / np.sqrt((z_current + 500) ** 2 + x_current ** 2))

                # creates 4 eddies
                # Eddy centered at bottom left corner (-400,-900)
                if x_current <= -300 and z_current <= -800:
                    radius = np.sqrt((z_current + 900) ** 2 + (x_current + 400) ** 2)
                    scale = .05

                    x_velocity = scale * radius * (
                                -(z_current + 900) / np.sqrt((z_current + 900) ** 2 + (x_current + 400) ** 2))
                    z_velocity = scale * radius * (
                                (x_current + 400) / np.sqrt((z_current + 900) ** 2 + (x_current + 400) ** 2))

                # Eddy centered at top left corner (-400,-100)
                elif x_current <= -300 and z_current >= -200:
                    radius = np.sqrt((z_current + 100) ** 2 + (x_current + 400) ** 2)
                    scale = .05

                    x_velocity = scale * radius * (
                                -(z_current + 100) / np.sqrt((z_current + 100) ** 2 + (x_current + 400) ** 2))
                    z_velocity = scale * radius * (
                                (x_current + 400) / np.sqrt((z_current + 100) ** 2 + (x_current + 400) ** 2))

                # Eddy centered at bottom right corner (400,-900)
                elif x_current >= 300 and z_current <= -800:
                    radius = np.sqrt((z_current + 900) ** 2 + (x_current - 400) ** 2)
                    scale = .05

                    x_velocity = scale * radius * (
                                -(z_current + 900) / np.sqrt((z_current + 900) ** 2 + (x_current - 400) ** 2))
                    z_velocity = scale * radius * (
                                (x_current - 400) / np.sqrt((z_current + 900) ** 2 + (x_current - 400) ** 2))

                # Eddy centered at top right corner (400,-100)
                elif x_current >= 300 and z_current >= -200:
                    radius = np.sqrt((z_current + 100) ** 2 + (x_current - 400) ** 2)
                    scale = .05

                    x_velocity = scale * radius * (
                                -(z_current + 100) / np.sqrt((z_current + 100) ** 2 + (x_current - 400) ** 2))
                    z_velocity = scale * radius * (
                                (x_current - 400) / np.sqrt((z_current + 100) ** 2 + (x_current - 400) ** 2))

                x_current = x_current + (x_velocity * self.Time_Step)
                z_current = z_current + (z_velocity * self.Time_Step)

                # Stopping when a polonium hits a wall
                if (x_current ** 2) + (y_current ** 2) >= self.x_max ** 2:
                    break

                self.sim_time = self.sim_time + self.Time_Step

            # polonium properties
            x2 = x_current
            y2 = y_current
            z2 = z_current

            s2 = [x2, y2, z2]

            po = par.Polonium(t2, s2)

            po.tmatch(rn)
            rn.tmatch(po)

            match(po, rn)

            self.Rnlist.append(rn)
            self.Polist.append(po)

            a = a + 1


def match(Polonium, Radon):
    if Polonium.time > Radon.time:
        if Polonium.matched == True:
            Polonium.partner.matched = False
        if Radon.matched == True:
            Radon.partner.matched = False

        Polonium.matched = True
        Radon.matched = True
        Polonium.partner = Radon
        Radon.partner = Polonium
        Polonium.timediff = Polonium.time - Polonium.partner.time
