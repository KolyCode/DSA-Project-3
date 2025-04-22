# a console-input implementation of pathfinding plots
# displays a 3d plotly plot in the user's browser

from plotter import *

print("Plotter for Path-Finding Algorithms (Dijkstra & A*)")
dim_in = input("Enter the x and y dimensions of the terrain to be generated as integers separated by a space: ").split()

# generate initial 3D heightmap
print("\nGenerating terrain with Perlin Noise...")
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
      \n\tHold `Right-Click` to pan""")
dists, prev = dijkstra(nodemap, start_node)
dijk_path = get_path(prev, end_node)
#dijk_path = [nodemap[0][0], nodemap[1][1], nodemap[2][1], nodemap[2][2]]  # temp : test case
a_star_path = a_star(start_node, end_node, nodemap)
#a_star_path = [nodemap[0][0], nodemap[1][1], nodemap[2][2], nodemap[2][3], nodemap[3][3], nodemap[4][4]]  # temp : test case

# add paths to surface
full_plot = addPathsToMap3d(terrain_plot, dijk_path, a_star_path)
full_plot.show()
