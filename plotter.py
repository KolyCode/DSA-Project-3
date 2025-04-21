# This file used directly in main.py to generate plotly objects for display
from map_creation import *  # provides heightmap
from path_finding import *
import plotly.graph_objects as go

def plotTerrain(as_3d=False):
    # on push of Plot Paths button

    # this function follows a call to create_maps(x,y)
    # heightmap: 2D numpy array of weights 0-255
    # nodemap: 2D array, entries are node objects with position, height, neighbor weight, path presence attributes

    # get x,y,z values from paths
    dijk_path = None#FIXME
    a_star_path = None#FIXME

    path1_x, path1_y, path1_z = [], [], []
    if dijk_path != None:
        for n in range(len(dijk_path)): 
            path1_x[n], path1_y[n], path1_z[n] = dijk_path[n].posx, dijk_path[n].posy, dijk_path[n].height
    path2_x, path2_y, path2_z = [], [], []
    if a_star_path != None:
        for n in range(len(a_star_path)):
            path2_x[n], path2_y[n], path2_z[n] = a_star_path[n].posx, a_star_path[n].posy, a_star_path[n].height

    #print(f"heightmap size : {heightmap.shape}")
    print(f"dijkstra path length : {len(path1_z)}\t a_star path length : {len(path2_z)}\t as_3d : {as_3d}")
    if as_3d == False:
        # heatmap plot
        # requires x, y arrays of paths
        fig = go.Figure()
        fig.add_trace(
            go.Heatmap(
                z = heightmap,
                colorscale = "Blackbody",
                text = [[str(height) for height in r] for r in heightmap],
                texttemplate="%{text}",
                textfont={"size":15}
            )
        )
        fig.add_trace( # path 1
            go.Scatter(
                x = path1_x,
                y = path1_y,
                mode = "lines+markers",
                line = dict(color="rgba(143, 0, 255, 0.6)", width=4),
                marker = dict(color="rgba(143, 0, 255, 0.6)", size=8),
                name = "Dijkstra"
            )
        )
        fig.add_trace( # path 2
            go.Scatter(
                x = path2_x,
                y = path2_y,
                mode = "lines+markers",
                line = dict(color="rgba(153, 187, 38, 0.6)", width=4),
                marker = dict(color="rgba(153, 187, 38, 0.6)", size=8),
                name = "A Star"
            )
        )
        fig.update_layout(
            title = "Heatmap of Generated Terrain and Paths",
            xaxis = dict(title="X"),
            yaxis = dict(title="Y")
        )
    else: 
        # 3d surface
        # requires path x, path y, path z (having values of height from heightmap)
        fig = go.Figure()
        fig.add_trace(
            go.Surface(
                z = heightmap,
                colorscale = "Blackbody"
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x = path1_x,
                y = path1_y,
                z = path1_z,
                mode = "lines+markers",
                line = dict(color="rgba(143, 0, 255, 0.6)", width=4),
                marker = dict(color="rgba(143, 0, 255, 0.6)", size=8),
                name = "Dijkstra"
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x = path2_x,
                y = path2_y,
                z = path2_z,
                mode = "lines+markers",
                line = dict(color="rgba(153, 187, 38, 0.6)", width=4),
                marker = dict(color="rgba(153, 187, 38, 0.6)", size=8),
                name = "A Star"
            )
        )
        fig.update_layout(
            title = "Surface Plot of Generated Terrain and Paths",
            scene = dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Height")
        )
        
    return fig

def clearPaths(): 
    # on push of Reset button
    pass
    
