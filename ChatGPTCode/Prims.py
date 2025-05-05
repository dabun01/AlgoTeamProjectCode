import time
import heapq
from typing import List, Tuple, Dict

def prim_mst(num_vertices: int,
             edges: List[Tuple[int, int, int]],
             start: int = 0
            ) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Prim’s algorithm for Minimum Spanning Tree using a min-heap.

    :param num_vertices: number of nodes labeled 0..n-1
    :param edges: list of undirected edges as (u, v, weight)
    :param start: starting node for the MST (default 0)
    :return: (mst_edges, total_weight)
    :time complexity: O(E log V), where
        V = number of vertices,
        E = number of edges
    """
    # Build adjacency list
    adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(num_vertices)}
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    visited = [False] * num_vertices
    mst_edges: List[Tuple[int, int, int]] = []
    total_weight = 0

    # Min-heap of crossing edges: (weight, from, to)
    min_heap: List[Tuple[int, int, int]] = []
    visited[start] = True
    for w, nbr in adj[start]:
        heapq.heappush(min_heap, (w, start, nbr))

    while min_heap and len(mst_edges) < num_vertices - 1:
        w, u, v = heapq.heappop(min_heap)
        if visited[v]:
            continue
        visited[v] = True
        mst_edges.append((u, v, w))
        total_weight += w
        for nw, nn in adj[v]:
            if not visited[nn]:
                heapq.heappush(min_heap, (nw, v, nn))

    return mst_edges, total_weight

# Same graph as before:
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4),
]
num_vertices = 4

# Measure execution time
start_time = time.perf_counter()
mst, weight = prim_mst(num_vertices, edges)
elapsed = time.perf_counter() - start_time

# Output results
print("MST edges:", mst)
print("Total weight:", weight)
print("Time complexity: O(E log V)   # here E=5, V=4 → O(5·log 4)")
print(f"Measured runtime: {elapsed:.6f} seconds")
