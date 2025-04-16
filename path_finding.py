"""
function Dijkstra(Graph, source):
    for each vertex v in Graph.Vertices:
        dist[v] ← INFINITY
        prev[v] ← UNDEFINED
        add v to Q
    dist[source] ← 0

    while Q is not empty:
        u ← vertex in Q with minimum dist[u]
        remove u from Q

        for each neighbor v of u still in Q:
            alt ← dist[u] + Graph.Edges(u, v)
            if alt < dist[v]:
                dist[v] ← alt
                prev[v] ← u
    return dist[], prev[]
"""
import heapq
from map_creation import *

def dijkstra(graph, start, end): #graph is a nodemap list
    dists = {}
    prev = {}
    nodes = []
    for r in graph:
        for v in r:
            dists[v] = float('inf')
            prev[v] = None
    dists[start] = 0
    for v in dists:
        heapq.heappush(nodes, (dists[v], v)) # add to nodes as a tuple (distance to node, node) so it's sorted by
        # the distances

    while nodes:
        dist, u = heapq.heappop(nodes) #pop the distance into dist and node into u

        if u == end:
            return dist, prev
        neigh = get_neighbors(u)
        for v, d in neigh:
            if v in nodes:
                alt = dist + d
                if alt < dists[v]:
                    dists[v] = alt
                    prev[v] = u
                    u.is_path = True
    return None # only gets here if theres no path

"""
function BellmanFord(list vertices, list edges, vertex source) is

    // This implementation takes in a graph, represented as
    // lists of vertices (represented as integers [0..n-1]) and edges,
    // and fills two arrays (distance and predecessor) holding
    // the shortest path from the source to each vertex

    distance := list of size n
    predecessor := list of size n

    // Step 1: initialize graph
    for each vertex v in vertices do
        // Initialize the distance to all vertices to infinity
        distance[v] := inf
        // And having a null predecessor
        predecessor[v] := null
    
    // The distance from the source to itself is zero
    distance[source] := 0

    // Step 2: relax edges repeatedly
    repeat |V|−1 times:
        for each edge (u, v) with weight w in edges do
            if distance[u] + w < distance[v] then
                distance[v] := distance[u] + w
                predecessor[v] := u


        NOT USING THIS PART, DONT HAVE NEGATIVE WEIGHT CYCLES
    // Step 3: check for negative-weight cycles
    for each edge (u, v) with weight w in edges do
        if distance[u] + w < distance[v] then
            predecessor[v] := u
            // A negative cycle exists; find a vertex on the cycle 
            visited := list of size n initialized with false
            visited[v] := true
            while not visited[u] do
                visited[u] := true
                u := predecessor[u]
            // u is a vertex in a negative cycle, find the cycle itself
            ncycle := [u]
            v := predecessor[u]
            while v != u do
                ncycle := concatenate([v], ncycle)
                v := predecessor[v]
            error "Graph contains a negative-weight cycle", ncycle
    return distance, predecessor
"""


def bellman(graph, start):
    dists = []
    prev = []
    for r in graph:
        for v in r:
            dists[v] = float('inf')
            prev[v] = None

    dists[start] = 0



