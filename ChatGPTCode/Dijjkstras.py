import heapq
import time
from typing import List, Tuple, Dict

def dijkstra_shortest_paths(
    num_vertices: int,
    edges: List[Tuple[int, int, int]],
    start: int
) -> Dict[int, float]:
    """
    Dijkstra’s algorithm for single-source shortest paths on a directed, weighted graph.

    :param num_vertices: number of vertices (0…n-1)
    :param edges: list of directed edges as (u, v, weight)
    :param start: the source vertex
    :return: dict mapping each vertex to its shortest‐path distance from start
    :time complexity: O(E log V), where
        V = number of vertices,
        E = number of edges
    """
    # build adjacency list
    adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(num_vertices)}
    for u, v, w in edges:
        adj[u].append((v, w))

    # initialize distances
    dist: Dict[int, float] = {i: float('inf') for i in range(num_vertices)}
    dist[start] = 0

    # min-heap of (distance, vertex)
    heap: List[Tuple[float, int]] = [(0, start)]

    while heap:
        d_u, u = heapq.heappop(heap)
        # skip stale entries
        if d_u > dist[u]:
            continue
        # relax outgoing edges
        for v, w in adj[u]:
            d_v = d_u + w
            if d_v < dist[v]:
                dist[v] = d_v
                heapq.heappush(heap, (d_v, v))

    return dist

if __name__ == "__main__":
    # Graph from your screenshot:
    # vertices 0–5, directed edges (u, v, weight):
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 5),
        (1, 3, 10),
        (2, 3, 3),
        (2, 4, 2),
        (3, 4, 4),
        (3, 5, 11),
        (4, 5, 8),
    ]
    num_vertices = 6
    start_node = 0

    # Measure actual execution time
    start_time = time.perf_counter()
    distances = dijkstra_shortest_paths(num_vertices, edges, start_node)
    end_time = time.perf_counter()
    elapsed = end_time - start_time

    # Output results
    print(f"Shortest‐path distances from {start_node}:")
    for v in range(num_vertices):
        print(f"  {start_node} → {v} = {distances[v]}")
    print(f"\nAlgorithmic time complexity: O(E log V)   # here E=9, V=6 → O(9·log 6)")
    print(f"Measured runtime: {elapsed:.6f} seconds")
