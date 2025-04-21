from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
import json
from plotly.utils import PlotlyJSONEncoder

#import everything from the other files (doing this to make the code cleaner & more readable)
from map_creation import *
from path_finding import *
#from plotter import *

# uvicorn main:app --reload

app = FastAPI()

# temporary - move to separate file
#create_maps() # input args x,y
#nodemap[x][y].height
#nodemap[x][y].isPath

# UI HTML
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/plot")
async def plot():
    pass

@app.post("/terrain-generator")
async def terrain_generator(xlim: int = Form(100), ylim: int = Form(100)):
    create_maps(xlim,ylim)

@app.post("/start-end-setter")
async def start_end_setter():
    pass
