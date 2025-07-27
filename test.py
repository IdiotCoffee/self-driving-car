import os
from canvas import Canvas
from network import Network
from racetrack import Track
from storage import Storage

# Network configuration
network_dimensions = 5, 4, 2  # input neurons, hidden layer neurons, output neurons

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(4), car_image_paths)
storage = Storage("brain.json")
networks = [Network(network_dimensions) for _ in range(4)]

best_chromosomes = storage.load()
for c, n in zip(best_chromosomes, networks):
    n.deserialize(c)
    
simulation_round = 1
while simulation_round <= 5 and canvas.is_simulating:
    canvas.simulate_generation(networks, simulation_round)
    simulation_round += 1