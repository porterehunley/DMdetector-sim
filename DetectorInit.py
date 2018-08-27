import CircularDetector as det
import VelocityField as vel
import Particles
import matplotlib as mpl
import _pickle as pickle
import matplotlib.pyplot as plt
def plotVectors2D(Arr, xmin, xmax, zmin, zmax): #Takes the array and the dimensions of the space and plots them
    X, Y, U, V = zip(*Arr)
    plt.figure(figsize=(10,10), dpi=80)
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=.2)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([zmin, zmax])
    plt.draw()
    plt.show()


Polist = []
Rnlist = []
detector = det.CircularDetector(1000)
detector.simulate()

with open('detector_sim_circle.pkl', 'wb') as output:
    pickle.dump(detector, output, -1)




