# Neural Network Car Simulation

This project is an application of neural networks using a genetic algorithm. It was created to gain a better understanding of both neural networks and genetic algorithms, following a course on Udemy (link: [Course Link](https://www.udemy.com/course/building-self-driving-cars-in-python-from-scratch/)).

## Overview

The program trains cars to navigate through different tracks using neural networks. The training process is enhanced by a genetic algorithm, which evolves the car's behavior over successive generations.

## Getting Started

### Training the Cars

1. **Training Script**: 
   - Run the `training.py` file to start training the cars.
   - The training data is stored in a file called `brain.json`.

2. **Choosing Tracks**:
   - Inside the `training.py` file, find the line:
     ```
     canvas = Canvas(Track(3), car_image_paths)
     ```
   - Replace the number `3` with any number between `0` and `3` to train the cars on different tracks.

3. **Training Process**:
   - Run the `training.py` simulation for all tracks (`0-3`) until at least 4 cars pass the checkpoint on each track.

### Testing the Cars

- Once training is complete, run the `test.py` file to see the cars navigate a brand new track using the knowledge they gained from the training tracks.

## Additional Features

- **Slipping Mechanism**: A slipping feature is implemented to ensure that cars slow down when they approach the edges of the track, simulating realistic driving conditions.

## Dependencies

- The only external library used in this project is `pyglet`, which is used to graphically draw the simulation of the cars. No other external libraries are required.

---

This project demonstrates how neural networks can be applied to autonomous driving simulations using genetic algorithms for optimization.
