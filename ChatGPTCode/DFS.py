import time
from typing import Any, Dict, List, Set

# Recursive DFS
def dfs_recursive(graph: Dict[Any, List[Any]], start: Any, visited: Set[Any]=None, order: List[Any]=None) -> List[Any]:
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for nbr in graph.get(start, []):
        if nbr not in visited:
            dfs_recursive(graph, nbr, visited, order)
    return order

# Iterative DFS
def dfs_iterative(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    visited: Set[Any] = set()
    order: List[Any] = []
    stack: List[Any] = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # push neighbors in reverse for consistent order
            for nbr in reversed(graph.get(node, [])):
                if nbr not in visited:
                    stack.append(nbr)
    return order

# Test graph
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]  # self-loop
}

# Measure recursive DFS
start_time = time.perf_counter()
rec_order = dfs_recursive(graph, 0)
rec_time = time.perf_counter() - start_time

# Measure iterative DFS
start_time = time.perf_counter()
iter_order = dfs_iterative(graph, 0)
iter_time = time.perf_counter() - start_time

# Output results
print("DFS Recursive Order:", rec_order)
print(f"Recursive DFS Measured Time: {rec_time:.6f} seconds\n")
print("DFS Iterative Order:", iter_order)
print(f"Iterative DFS Measured Time: {iter_time:.6f} seconds")
