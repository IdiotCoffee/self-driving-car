import os
from canvas import Canvas
from network import Network
from racetrack import Track
from storage import Storage

# Network configuration
network_dimensions = 5, 4, 2  # input neurons, hidden layer neurons, output neurons

car_images = [os.path.join("images", f"car{i}.png") for i in (0, 1, 2, 3, 4)]
canvas = Canvas(Track(4), car_images)
storage = Storage("brain.json")
networks = [Network(network_dimensions) for _ in range(4)]

best_chromosomes = storage.load()
for c, n in zip(best_chromosomes, networks):
    n.deserialize(c)
    
simulation_round = 1
while canvas.is_simulating:
    canvas.simulate_generation(networks, simulation_round)