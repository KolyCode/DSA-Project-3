# Interactive Web App for Path-Finding Algorithms — DSA-Project-3
### created in the genius minds of:
* Alexander Kolychkine
* Matteo Welford
* Jaden Despeines

Demo: https://youtu.be/ExpqaN0ktnQ

This is a web app designed to showcase the use of two algorithms in navigation on a heightmap: **Dijkstra's algorithm** and the **A\* algorithm**. The user can enter the dimensions of the heightmap, which is randomly generated with Perlin noise, followed by the coordinates of their starting and ending point on the heightmap. The application plots the path devised by each algorithm.

For each algorithm, the randomly generated terrain of the heightmap is a graph of nodes that are connected to their lateral and diagonal neighbors. The weight between two nodes used to determine the cost of a path is the direct distance in three-dimensional space (In essence, this is the hypoteneuse of a right triangle whose other sides are the horizontal and vertical distances between nodes in space).

### DEVELOPER INSTRUCTIONS

**Project Implementation**
* disregard templates/ and main.py in assessment of code count

plot_tester.py implements the plotting functionality for this project with console input. 

Run file `plot_tester.py`

You may need to install a package like noise with `pip install noise`. 
Try the following in **TERMINAL** if you receive errors related to absent packages for functions
```
python -m venv env
source env/bin/activate  # On Mac/Linux
env\Scripts\activate      # On Windows
pip install -r requirements.txt
```

Follow the instructions of the text prompts to input terrain size bounds and starting and ending point positions.
The program generates a Plotly 3D surface that can be viewed and interacted with in a browser tab.

---

**Work in progress web app implementation**

**Ignore instructions below, alternative web app in main.py is not yet in a working state:** 

> To test the web app within your browser, open **TERMINAL** and execute:
> ```
> uvicorn main:app --reload
> ```
> A link for locally accessing the app will be generated.
> > NOTE: You can do this very conveniently inside a GitHub Codespace
> 
> Be sure to fill all the fields with valid numerical values before attempting to plot. After entering plot dimensions, click "Generate Map." After entering start and endpoint coordinates within those dimensions, click "Plot Paths." Enjoy!
