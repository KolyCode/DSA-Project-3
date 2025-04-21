# Interactive Web App for Path-Finding Algorithms — DSA-Project-3
### created in the genius minds of:
* Alexander Kolychkine
* Matteo Welford
* Jaden Despeines

This is a web app designed to showcase the use of two algorithms in navigation on a heightmap: **Dijkstra's algorithm** and the **A\* algorithm**. The user can enter the dimensions of the heightmap, which is randomly generated with Perlin noise, followed by the coordinates of their starting and ending point on the heightmap. The application plots the path devised by each algorithm.

### DEVELOPER INSTRUCTIONS
To test this web app within your browser, open **TERMINAL** and execute:
```
uvicorn main:app --reload
```
A link for locally accessing the app will be generated.
> NOTE: You can do this very conveniently inside a GitHub Codespace

Be sure to fill all the fields with valid numerical values before attempting to plot. After entering plot dimensions, click "Generate Map." After entering start and endpoint coordinates within those dimensions, click "Plot Paths." Enjoy!

base requirements (temp note -- delete later after requirements.txt implemented and revised):
fastapi, plotly, uvicorn
json, matplotlib, noise, numpy, random, math, heapq