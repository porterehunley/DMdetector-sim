import VelocityField as vel
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

with open('detector_sim_circle.pkl', 'rb') as input:
    detector = pickle.load(input)

Rnlist = detector.Rnlist
Polist = detector.Polist




field = vel.vectorField(Polist)
big = field.vectorize(False)
plotVectors2D(big,-500,500,-1000,0)
field.reconstruct()
big = field.vectorize(False)
plotVectors2D(big,-500,500,-1000,0)