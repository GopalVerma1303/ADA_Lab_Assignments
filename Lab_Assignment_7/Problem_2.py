import heapq


def prims(graph, start):
    """Return the minimum spanning tree of a weighted graph using Prim's algorithm."""
    mst = set()  # set of edges in the minimum spanning tree
    visited = set([start])  # set of vertices visited so far
    edges = [(weight, start, to) for to, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.add((frm, to, weight))
            for to_next, weight_next in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight_next, to, to_next))

    return mst
