import heapq, math

from map_creation import *

def dijkstra(graph, start): #graph is a nodemap list
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
        neigh = get_neighbors(u)
        for v, d in neigh:
            if v in nodes:
                alt = dist + d
                if alt < dists[v]:
                    dists[v] = alt
                    prev[v] = u
                    u.is_path = True

    return dists, prev # use get_path with this to find the best overall path to wherever

def get_path(prev, cur):
    path = [cur]
    while cur in prev:
        cur = prev[cur]
        path.insert(0, cur)
    return path

#heuristic function, estimates the distance by using a straight line function
def heuristic(start, end):
    return math.sqrt((start.posx - end.posx) ** 2 + (start.posy - end.posy) ** 2)


def a_star(start, end, graph):
    open_set = []
    heapq.heappush(open_set, (0, start))
    prev = {}

    #g_score[n] is the currently known least cost to n
    g_score = {start: 0}

    #f_score[n] is g_score[n] + h(n), represents our current best guess of
    # how cheap a path start to end is going through n
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set) #don't need the first part of this, its just for sorting

        if current == end:
            return get_path(prev, current)

        for d, n in get_neighbors(current):
            tentative_g_score = g_score[current] + d
            if tentative_g_score < g_score[n]:
                prev[n] = current
                g_score[n] = tentative_g_score
                f_score[n] = tentative_g_score + heuristic(n, end)
                if n not in open_set:
                    heapq.heappush(open_set, (f_score[n], n))

    # open_set is empty but the goal wasn't reached, i.e. no path
    return None









