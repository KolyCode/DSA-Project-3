#created by Alexander Kolychkine
import matplotlib.pyplot as plt
from noise import pnoise2
import numpy as np
import random
import math

# this is the height map:
heightmap = None
#this is the node map:
nodemap = None


#START NODE CLASS
#START NODE CLASS
#START NODE CLASS
#START NODE CLASS
#START NODE CLASS
class Node:
    def __init__(self, posx, posy, height):
        self.posx = posx        #x-coordinate of the node
        self.posy = posy        #y-coordinate of the node
        self.height = height    #height of the node
        self.isPath = False     #is true if this node is part of the path

        #these are defined when find_distance_to_neighbors() is called
        self.weight_upleft = None
        self.weight_up = None
        self.weight_upright = None
        self.weight_left = None
        self.weight_right = None
        self.weight_downleft = None
        self.weight_down = None
        self.weight_downright = None

    #this is basically constructor part two
    def find_distance_to_neighbors(self):
        self.weight_upleft = self.find_upleft()
        self.weight_up = self.find_up()
        self.weight_upright = self.find_upright()
        self.weight_left = self.find_left()
        self.weight_right = self.find_right()
        self.weight_downleft = self.find_downleft()
        self.weight_down = self.find_down()
        self.weight_downright = self.find_downright()

    #these are the cardinal find functions
    def find_up(self):
        if does_node_exist(self.posx, self.posy + 1):
            height_up = heightmap[self.posx][self.posy + 1]  # this is just an int number representing up's height
            weight_to_up = calculate_weight(self, height_up)
            return weight_to_up
        return None  # if the node does not exist
    def find_down(self):
        if does_node_exist(self.posx, self.posy - 1):
            height_down = heightmap[self.posx][self.posy - 1]  # this is just an int number representing down's height
            weight_to_down = calculate_weight(self, height_down)
            return weight_to_down
        return None  # if the node does not exist
    def find_left(self):
        if does_node_exist(self.posx - 1, self.posy):
            height_left = heightmap[self.posx - 1][self.posy]  # this is just an int number representing left's height
            weight_to_left = calculate_weight(self, height_left)
            return weight_to_left
        return None  # if the node does not exist
    def find_right(self):
        if does_node_exist(self.posx + 1, self.posy):
            height_right = heightmap[self.posx + 1][self.posy]  # this is just an int number representing right's height
            weight_to_right = calculate_weight(self, height_right)
            return weight_to_right
        return None  # if the node does not exist

    #these are the diagonal find functions
    def find_upleft(self):
        if does_node_exist(self.posx-1, self.posy+1):
            height_upleft = heightmap[self.posx-1][self.posy+1] #this is just an int number representing upleft's height
            weight_to_upleft = calculate_weight_diagonal(self, height_upleft)
            return weight_to_upleft
        return None #if the node does not exist
    def find_upright(self):
        if does_node_exist(self.posx+1, self.posy+1):
            height_upright = heightmap[self.posx+1][self.posy+1] #this is just an int number representing upright's height
            weight_to_upright = calculate_weight_diagonal(self, height_upright)
            return weight_to_upright
        return None #if the node does not exist
    def find_downleft(self):
        if does_node_exist(self.posx-1, self.posy-1):
            height_downleft = heightmap[self.posx-1][self.posy-1] #this is just an int number representing downleft's height
            weight_to_downleft = calculate_weight_diagonal(self, height_downleft)
            return weight_to_downleft
        return None #if the node does not exist
    def find_downright(self):
        if does_node_exist(self.posx+1, self.posy-1):
            height_downright = heightmap[self.posx+1][self.posy-1] #this is just an int number representing downright's height
            weight_to_downright = calculate_weight_diagonal(self, height_downright)
            return weight_to_downright
        return None #if the node does not exist

#helper function to determine whether or not a node exists
def does_node_exist(x, y):
    if(x >= 0 and x < len(heightmap) and y >= 0 and y < len(heightmap[0])):
        return True
    return False

def calculate_weight(start, end, distance=1.0):
    delta_height = end - start.height
    delta_height_normalized = (delta_height / 255.0) * 2 - 1 #normalizes delta height from 0-255 to -1 to 1, which is useful for our calculations

    hypotenuse = math.sqrt(distance * distance + delta_height_normalized * delta_height_normalized) #uses the knowledge of pythagoras to calculate the 3D distance between points

    weight = 0.0

    if delta_height >= 0:
        weight = hypotenuse
    else:
        weight = distance - (hypotenuse - distance)

    return weight

#helper function for use in finding diagonal weights; calls calculate weight with distance sqrt(2) instead of 1
def calculate_weight_diagonal(start, end):
    return calculate_weight(start, end, distance=1.4142)
#END NODE CLASS
#END NODE CLASS
#END NODE CLASS
#END NODE CLASS
#END NODE CLASS


#creates both the height and node maps:
def create_maps(size_x=400, size_y=400):
    create_height_map(size_x, size_y)
    create_node_map()
    display_height_map() #comment this out if you want to stop generating the terrain images

#creates heightmap, which is an array of integers representing the heights
def create_height_map(x_length=400, y_length=400):
    global heightmap

    array = (x_length, y_length)

    #DO NOT CHANGE THESE PRESET VALUES. I HAVE THEM THIS WAY FOR A REASON!
    seed = random.randint(-2048, 2047) #chooses the seed for the perlin noise generation
    scale = random.randint(50,200) #smaller = more zoomed in. gives a random level of zoom
    num_octaves = random.randint(1,126); #random level of detail, more octaves = more detail & less height variation
    print(seed, scale, num_octaves)

    heightmap = np.zeros(array)

    for i in range(array[0]):
        for j in range(array[1]):
            heightmap[i][j] = pnoise2(i / scale, j / scale, octaves=num_octaves, base=seed)

    # Normalize to 0–255
    heightmap = ((heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())) * 255
    heightmap = np.nan_to_num(heightmap, nan=0, posinf=0, neginf=0) #take away goofy numbers
    heightmap = heightmap.astype(int)

    return heightmap

def display_height_map():
    #creates the map which is displayed
    plt.imshow(heightmap, cmap='terrain')
    plt.colorbar(label='Elevation (ft)')
    plt.title("Perlin Noise Terrain")
    plt.gca().invert_yaxis()
    plt.show()

#creates the node_map, which is an array of nodes
def create_node_map():
    nodemap = [[None for _ in range(len(heightmap[0]))] for _ in range(len(heightmap))]
    #this for loop initializes the node array
    for x in range(0, len(heightmap)):
        for y in range(0, len(heightmap[x])):
            nodemap[x][y] = Node(x, y, heightmap[x][y])

    #this for loop calls the neighbor calculations for each node
    for x in range(len(nodemap)):
        for y in range(len(nodemap[x])):
            nodemap[x][y].find_distance_to_neighbors()

    #it also edits the nodemap, so u don't have to take the return here if you don't want to
    return nodemap





