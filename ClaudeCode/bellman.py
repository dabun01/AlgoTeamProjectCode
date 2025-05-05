import time

def bellman_ford(graph, source):
    """
    Find shortest paths from source vertex to all vertices in the graph
    
    Args:
        graph: Dictionary representing an adjacency list with weights
              Format: {node: [(neighbor, weight), ...], ...}
        source: Source vertex
    
    Returns:
        distances: Dictionary with shortest distances to each vertex
        predecessors: Dictionary with predecessor of each vertex in shortest path
        negative_cycle: Boolean indicating if a negative cycle was detected
    """
    # Step 1: Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    
    predecessors = {vertex: None for vertex in graph}
    
    # Get all edges from the graph
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((u, v, weight))
    
    # Step 2: Relax all edges |V| - 1 times
    # Where |V| is the number of vertices
    num_vertices = len(graph)
    
    for _ in range(num_vertices - 1):
        for u, v, weight in edges:
            # If the distance to u is not infinity and we can improve
            # the distance to v by going through u
            if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
    
    # Step 3: Check for negative-weight cycles
    # If we can still relax edges, then there is a negative cycle
    negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
            negative_cycle = True
            break
    
    return distances, predecessors, negative_cycle

def get_shortest_path(predecessors, source, target):
    """
    Reconstruct the shortest path from source to target
    
    Args:
        predecessors: Dictionary with predecessor of each vertex
        source: Source vertex
        target: Target vertex
    
    Returns:
        path: List representing the shortest path from source to target
    """
    path = []
    current = target
    
    # If there's no path to the target vertex
    if predecessors[target] is None and source != target:
        return path
    
    # Reconstruct the path from target to source
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    # Reverse the path to get source to target
    return path[::-1]

# Helper function to create a graph from a list of edges
def create_graph_from_edges(edges):
    """
    Create a graph from a list of weighted edges
    
    Args:
        edges: List of edges in the format (u, v, weight)
    
    Returns:
        graph: Dictionary representing an adjacency list with weights
    """
    graph = {}
    
    # Get all unique vertices
    vertices = set()
    for u, v, _ in edges:
        vertices.add(u)
        vertices.add(v)
    
    # Initialize the graph with empty adjacency lists
    for vertex in vertices:
        graph[vertex] = []
    
    # Add edges to the graph
    for u, v, weight in edges:
        graph[u].append((v, weight))
    
    return graph

# Example usage
if __name__ == "__main__":
    # Example graph represented as a list of edges: (u, v, weight)
    # This graph includes a negative edge but no negative cycle
    edges = [
        ('A', 'B', -1),
        ('A', 'C', 4),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 2),
        ('D', 'C', 5),
        ('D', 'B', 1),
        ('E', 'D', -3)
    ]
    
    # Create the graph
    graph = create_graph_from_edges(edges)
    
    # Choose a source vertex
    source_vertex = 'A'
    
    # Find shortest paths
    start_time = time.time()
    distances, predecessors, has_negative_cycle = bellman_ford(graph, source_vertex)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for Bellman-Ford algorithm: {elapsed_time:.6f} seconds")
    
    if has_negative_cycle:
        print("Graph contains a negative cycle, shortest paths may not be defined.")
    else:
        # Print shortest distances
        print(f"Shortest distances from vertex {source_vertex}:")
        for vertex, distance in distances.items():
            print(f"To vertex {vertex}: {distance}")
        
        # Print shortest paths
        print(f"\nShortest paths from vertex {source_vertex}:")
        for vertex in graph:
            if vertex != source_vertex:
                path = get_shortest_path(predecessors, source_vertex, vertex)
                if path:
                    print(f"To vertex {vertex}: {' -> '.join(map(str, path))}")
                else:
                    print(f"No path to vertex {vertex}")