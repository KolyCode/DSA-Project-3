#this does the same thing as map_creation.py but it does the whole thing using an adjacency list
#btw a python dictionary is just a map

#this is a dictionary, representing a map
from map_creation import Node
nodemap = {}

def create_node_map(length_x=400, length_y=400):
    for i in range(length_x*length_y):
        nodemap[i] = []

    
