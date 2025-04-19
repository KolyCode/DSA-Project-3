# This file used directly in main.py to generate plotly objects for display
from map_creation import *  # provides heightmap
from path_finding import *
import plotly.graph_objects as go

paths = {} # dictionary, {name of path finding algo : 2d array of locations on path}

def plotTerrain(as_3d=False):
    # on push of Plot Paths button

    # this function follows a call to create_maps(x,y)
    # heightmap: 2D numpy array of weights 0-255
    # nodemap: 2D array, entries are node objects with position, height, neighbor weight, path presence attributes

    # get x,y,z values from paths
    dijk_path = None#FIXME
    a_star_path = None#FIXME
    # tuple implementation : result = [(n.posx, n.posy, n.height) for n in dijk_path]
    for n in dijk_path: 
        path1_x, path1_y, path1_z = n.posx, n.posy, n.height
    for n in a_star_path:
        path2_x, path2_y, path2_z = n.posx, n.posy, n.height

    if as_3d = False:
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
                name = "P1"
            )
        )
        fig.add_trace( # path 2
            go.Scatter(
                x = path2_x,
                y = path2_y,
                mode = "lines+markers",
                line = dict(color="rgba(153, 187, 38, 0.6)", width=4),
                marker = dict(color="rgba(153, 187, 38, 0.6)", size=8),
                name = "P2"
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
            go.Scatter3D(
                x = path1_x,
                y = path1_y,
                z = path1_z,
                mode = "lines+markers",
                line = dict(color="rgba(143, 0, 255, 0.6)", width=4),
                marker = dict(color="rgba(143, 0, 255, 0.6)", size=8),
                name = "P1"
            )
        )
        fig.add_trace(
            go.Scatter3D(
                x = path2_x,
                y = path2_y,
                z = path2_z,
                mode = "lines+markers",
                line = dict(color="rgba(153, 187, 38, 0.6)", width=4),
                marker = dict(color="rgba(153, 187, 38, 0.6)", size=8),
                name = "P2"
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
    
