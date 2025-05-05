import time
from typing import List, Tuple, Dict

class UnionFind:
    """Union-find (disjoint set) with path compression & union by rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def kruskal_mst(num_vertices: int, edges: List[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Kruskal’s MST.
    :param num_vertices: number of nodes (0…n-1)
    :param edges: list of tuples (u, v, weight)
    :return: (mst_edges, total_weight)
    :time complexity: O(E log E), dominated by sorting the edges
    """
    edges_sorted = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(num_vertices)

    mst_edges = []
    total_weight = 0
    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == num_vertices - 1:
                break

    return mst_edges, total_weight

# Graph from screenshot:
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
mst, weight = kruskal_mst(num_vertices, edges)
elapsed = time.perf_counter() - start_time

# Output results
print("MST edges:", mst)
print("Total weight:", weight)
print("Time complexity: O(E log E)   # here E=5 edges → sorting dominates")
print(f"Measured runtime: {elapsed:.6f} seconds")
