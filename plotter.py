# This file used directly in main.py to generate plotly objects for display
from map_creation import *  # provides heightmap
from path_finding import *
import plotly.graph_objects as go

# color maps for heightmap
# alternatively, colorscale = "Blackbody", colorscale = "Rainbow"
elevation_colorscale = [
    [0.0, "darkblue"],
    [0.2, "darkgreen"],
    [0.3, "green"],
    [0.4, "lightgreen"],
    [0.5, "yellow"],
    [0.5, "gray"],
    [1.0, "white"]
]
# resembles Apple Maps Satellite View
elevation_colorscale_2 = [
    [0.0, "darkgreen"],
    [0.2, "green"],
    [0.4, "tan"],
    [0.6, "brown"],
    [0.8, "gray"],
    [1.0, "white"]
]
# resembles Google Satellite Maps
elevation_colorscale_3 = [
    [0.0, "green"],
    [0.2, "lightgreen"],
    [0.4, "yellow"],
    [0.6, "saddlebrown"],
    [0.8, "darkbrown"],
    [1.0, "white"]
]

def plotMap3d(heightmap):
    # 3d surface
    fig = go.Figure()
    fig.add_trace(
        go.Surface(
            z = heightmap,
            #colorscale = "Blackbody"
            colorscale = elevation_colorscale_2
        )
    )
    fig.update_layout(
        title = "Surface Plot of Generated Terrain and Paths",
        scene = dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Elevation", zaxis=dict(range=[0,255]))
    )
    return fig

def addPathsToMap3d(fig, dijk_path, a_star_path):
    # generate lists of values x,y,z in paths
    path1_x, path1_y, path1_z = [], [], []
    if dijk_path != None:
        for n in range(len(dijk_path)): 
            path1_x.append(dijk_path[n].posx)
            path1_y.append(dijk_path[n].posy)
            path1_z.append(dijk_path[n].height*1.15)
    path2_x, path2_y, path2_z = [], [], []
    if a_star_path != None:
        for n in range(len(a_star_path)):
            path2_x.append(a_star_path[n].posx)
            path2_y.append(a_star_path[n].posy)
            path2_z.append(a_star_path[n].height*1.15)

    # plot Dijkstra path
    fig.add_trace(
        go.Scatter3d(
            x = path1_x,
            y = path1_y,
            z = path1_z,
            mode = "lines+markers",
            line = dict(color="rgba(143, 0, 255, 0.6)", width=10),
            marker = dict(color="rgba(143, 0, 255, 0.6)", size=12),
            name = "Dijkstra"
        )
    )
    # plot A* path
    fig.add_trace(
        go.Scatter3d(
            x = path2_x,
            y = path2_y,
            z = path2_z,
            mode = "lines+markers",
            line = dict(color="rgba(153, 187, 38, 0.6)", width=10),
            marker = dict(color="rgba(153, 187, 38, 0.6)", size=12),
            name = "A Star"
        )
    )

    # mark start and end points
    fig.add_trace(
        go.Scatter3d(
            x=[path1_x[0]], y=[path1_y[0]], z=[path1_z[0]],
            mode="markers+text",
            marker={"size":12,"color":"green"},
            text=["Start"],
            name="Start Point",
            textposition="top center"
        )
    )
    fig.add_trace(
        go.Scatter3d(
            x=[path1_x[-1]], y=[path1_y[-1]], z=[path1_z[-1]],
            mode="markers+text",
            marker={"size":12,"color":"red"},
            text=["End"],
            name="End Point",
            textposition="top center"
        )
    )

    path_annotation = f"""
Dijkstra Path Length :  {len(dijk_path)}<br>
A* Path Length :  {len(a_star_path)}
"""
    fig.update_layout(
        # position legend in bottom left
        legend=dict(
            x=0.05,
            y=0.1
        ),
        # print path lengths over plot
        annotations=[
            dict(
                x=0.05, y=0.9,
                xref="paper", yref="paper",
                text=path_annotation,
                font={"size":14,"color":"black"},
                xanchor="left",
                showarrow=False,
                bgcolor="white",
                bordercolor="white"
            )
        ]
    )
    return fig