# Particle Simulation and Decay Matching

The goal of this project is to accurately pair decaying radon atoms with their polonium offspring and reconstruct the resulting velocity. The code is modeled and written for the XENON1T darkmatter detector at Purdue University. The project is divided into three parts: simulation and reconstruction. 

#### Simulation
The simulation begins in the CircularDetector.py file. The code first simulates the decay of x number of Radons. The decayed radons are given a random location and a velocity based on that location. In addition, they are also given a lifetime based on a previously derived probability function. It then runs the radon through the velocity field in small time increments until the counter reaches the lifetime given to the radon. At the end of its lifetime, the radon decays into a polonium and all relevant data is stored.


#### Reconstruction

Reconstruction starts in VelocityField.py and is run from VelReconstruction. The VelocityField class takes in a list of poloniums from the simulation that was run before. The velocity field first filters through the list of Poloniums and saves those who’s previous radon decay is close to the polonium in both time and position. These are so close together, that we can safely draw a straight vector between the two events; these poloniums are called constructors because they will be used to help build the rest of the velocity field. 

Once all of the constructors are known, VelocityField uses Ball.py to try and match the pairs that are farther away based on the constructors’ velocities. The ball acts as a probe, it averages the velocities of the constructors around it, then, by small time increments, the ball travels across the detector and stops after a certain amount of time. We place the ball on the poloniums whose radon is too far away for the velocity vector to be drawn, and then send it on its way to see where it lands. If it lands on the radon, then we can add another velocity vector.

After everything is run, the velocity field outputs the data to an array to visualize the new velocity field. 


## Getting Started

The repository is in the form of a PyCharm project. You can either download everything and load it into PyCharm as a new project, or you can just download the source code. 
### Prerequisites

You must have Matplotlib and Numpy installed for it to run properly. 


## Running the tests

First run DetectorInit.py, this will create all the data that will be used to reconstruct the velocity field. Then run VelReconstruction.py.

First you will see an initial vecotor field, take note and close. After, you will see a "reconstructed" velocity field. 



