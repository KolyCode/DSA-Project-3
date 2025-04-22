# a console-input implementation of pathfinding plots
# displays a 3d plotly plot in the user's browser

from plotter import *

print("Plotter for Path-Finding Algorithms (Dijkstra & A*)")
dim_in = input("Enter the x and y dimensions of the terrain to be generated as integers separated by a space: ").split()

# generate initial 3D heightmap
print(f"\nGenerating terrain ({int(dim_in[0])*int(dim_in[1])} points) with Perlin Noise...")
heightmap = create_height_map(int(dim_in[0]), int(dim_in[1]))
nodemap = create_node_map_from_heightmap(heightmap)
terrain_plot = plotMap3d(heightmap)
#terrain_plot.show()  # display just terrain

# input start / end
start_in = input("Enter the x and y dimensions of the starting point, separated by a space: ").split()
start_in = (int(start_in[0]), int(start_in[1]))
end_in = input("Enter the x and y dimensions of the destination point, separated by a space: ").split()
end_in = (int(end_in[0]), int(end_in[1]))

start_node = nodemap[int(start_in[0])][int(start_in[1])]
end_node = nodemap[int(end_in[0])][int(end_in[1])]

# generate paths
print("""\nDisplaying Terrain and Paths in Plotly... 
      \n\tHold `Left-Click` to rotate
      \n\tUse `Scroll Wheel` to zoom
      \n\tHold `Right-Click` to pan\n""")

def path_cost(path):
      cost = 0
      for i in range(len(path)-1):
           lateral_dist = (abs(path[i].posx - path[i+1].posx)**2 + abs(path[i].posy - path[i+1].posy)**2)**0.5
           vert_dist = abs(path[i].height - path[i+1].height)
           direct_dist = (lateral_dist**2 + vert_dist**2)**0.5
           cost += direct_dist
      return cost

dists, prev = dijkstra(nodemap, start_node)
dijk_path = get_path(prev, end_node)[1:]
dijk_path_cost = path_cost(dijk_path)
#print(f"Dijkstra Path\n\tEdge Count :  {len(dijk_path)}\n\tCost       :   {dijk_path_cost}")

a_star_path = a_star(start_node, end_node, nodemap)
a_star_path_cost = path_cost(a_star_path)
#print(f"A* Path\n\tEdge Count :  {len(a_star_path)}\n\tCost       :  {a_star_path_cost}")

# add paths to surface
full_plot = addPathsToMap3d(terrain_plot, dijk_path, a_star_path)
full_plot.show()
