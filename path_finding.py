"""function Dijkstra(Graph, source):
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
    return None # only gets here if theres no path

