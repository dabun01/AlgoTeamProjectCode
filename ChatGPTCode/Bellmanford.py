import time
from typing import List, Tuple, Dict

def bellman_ford(
    num_vertices: int,
    edges: List[Tuple[int, int, int]],
    start: int
) -> Dict[int, float]:
    """
    Bellman–Ford algorithm for single-source shortest paths on a directed, weighted graph.

    :param num_vertices: number of vertices (0…n-1)
    :param edges: list of directed edges as (u, v, weight)
    :param start: the source vertex
    :return: dict mapping each vertex to its shortest-path distance from start
    :time complexity: O(V * E), where
        V = number of vertices,
        E = number of edges
    """
    # Initialization
    dist: Dict[int, float] = {i: float('inf') for i in range(num_vertices)}
    dist[start] = 0

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Check for negative‐weight cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative‐weight cycle")

    return dist

if __name__ == "__main__":
    # Same directed graph as in Dijkstra's example:
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

    # Measure execution time
    start_time = time.perf_counter()
    distances = bellman_ford(num_vertices, edges, start_node)
    elapsed = time.perf_counter() - start_time

    # Output results
    print(f"Shortest-path distances from {start_node}:")
    for v in range(num_vertices):
        print(f"  {start_node} → {v} = {distances[v]}")

    print(f"\nAlgorithmic time complexity: O(V·E)   # here V=6, E=9 → O(6·9)")
    print(f"Measured runtime: {elapsed:.6f} seconds")
