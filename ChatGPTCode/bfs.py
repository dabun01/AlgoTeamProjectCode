import time
from collections import deque
from typing import List, Dict, Any, Set

def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform a breadth-first traversal on a graph.

    :param graph: adjacency list mapping each node to its neighbors
    :param start: the node from which to start the traversal
    :return: list of nodes in the order they were first visited
    :time complexity: O(V + E), where
        V = number of vertices in the graph,
        E = number of edges in the graph
    """
    visited: Set[Any] = {start}
    queue: deque[Any] = deque([start])
    order: List[Any] = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)

    return order

# Specific test graph:
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]     # self-loop
}

if __name__ == "__main__":
    start_time = time.perf_counter()
    traversal = bfs(graph, 0)
    elapsed = time.perf_counter() - start_time

    print("BFS traversal order:", traversal)
    print("Time complexity: O(V + E)   # here V=4, E=6 for your test graph → O(4 + 6)")
    print(f"Measured runtime: {elapsed:.6f} seconds")
