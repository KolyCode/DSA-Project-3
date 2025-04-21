from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
import json
from plotly.utils import PlotlyJSONEncoder

#import everything from the other files (doing this to make the code cleaner & more readable)
from map_creation import *
from path_finding import *
from plotter import *

# TERMINAL: uvicorn main:app --reload
app = FastAPI()
heightmap_fig = go.Figure()

# temporary notes
#create_maps() # input args x,y
#nodemap[x][y].height
#nodemap[x][y].isPath

# UI HTML
@app.get("/", response_class=HTMLResponse)
async def root():
    print("accessing \"/\"...")  # debug
    with open("templates/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/plot")
async def plot():
    print("accessing \"/plot\"...")

@app.post("/terrain-generator")
async def terrain_generator(xlim: int = Form(100), ylim: int = Form(100)):
    print("accessing \"/terrain-generator\"...")
    # create and plot just heightmap
    create_maps(xlim,ylim)  # prints seed, scale, num of octaves
    global heightmap_fig
    heightmap_fig = plotTerrain(as_3d=True)
    heightmap_fig = json.dumps(heightmap_fig, cls=PlotlyJSONEncoder)
    return JSONResponse(content=heightmap_fig)

@app.post("/start-end-setter")
async def start_end_setter():
    print("accessing \"/start-end-setter\"...")
    # plot heightmap and points/paths
    global heightmap_fig
    marked_fig = heightmap_fig
    ##marked_fig.add_trace()##
    #marked_fig = json.dumps(marked_fig, cls=PlotlyJSONEncoder)
    #return JSONResponse(content=marked_fig)

@app.post("/reset-button")
async def reset_button():
    print("accessing \"/reset-button\"...")
    # remove points/paths, reset to heightmap
    global heightmap_fig
    heightmap_fig = plotTerrain(as_3d=True)
    heightmap_fig = json.dumps(heightmap_fig, cls=PlotlyJSONEncoder)
    return JSONResponse(content=heightmap_fig)
