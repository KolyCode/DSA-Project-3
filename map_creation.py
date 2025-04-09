#created by Alexander Kolychkine
import matplotlib.pyplot as plt
from noise import pnoise2
import numpy as np
import random

#DO NOT CHANGE THESE
MIN_INT = -2048
MAX_INT = 2047

#this is the height map:
heightmap = None

def create_height_map(x_length = 400, y_length = 400):
    array = (x_length, y_length)

    seed = random.randint(MIN_INT, MAX_INT) #chooses the seed for the perlin noise generation
    scale = random.randint(50,200) #smaller = more zoomed in. gives a random level of zoom
    num_octaves = random.randint(1,126); #random level of detail, more octaves = more detail & less height variation
    print(seed, scale, num_octaves)

    terrain = np.zeros(array)

    for i in range(array[0]):
        for j in range(array[1]):
            terrain[i][j] = pnoise2(i / scale, j / scale, octaves=num_octaves, base=seed)

    # Normalize to 0–255
    terrain = ((terrain - terrain.min()) / (terrain.max() - terrain.min())) * 255
    #terrain = np.nan_to_num(terrain, nan=0, posinf=0, neginf=0) #take away goofy numbers
    terrain = terrain.astype(int)

    #creates the map which is displayed
    plt.imshow(terrain, cmap='terrain')
    plt.colorbar(label='Elevation (m)')
    plt.title("Perlin Noise Terrain")
    plt.show()

    heightmap = terrain
    return terrain