import heapq
import time
def dijkstra(graph, start):
    """
    Find shortest paths from start vertex to all vertices in the graph
    
    Args:
        graph: Dictionary representing an adjacency list with weights
              Format: {node: [(neighbor, weight), ...], ...}
        start: Starting vertex
    
    Returns:
        distances: Dictionary with shortest distances to each vertex
        predecessors: Dictionary with predecessor of each vertex in the shortest path
    """
    # Initialize distances with infinity for all vertices except the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Dictionary to store the predecessor of each vertex in the shortest path
    predecessors = {vertex: None for vertex in graph}
    
    # Priority queue to determine which vertex to process next
    # Format: (distance, vertex)
    priority_queue = [(0, start)]
    
    # Set to keep track of processed vertices
    processed = set()
    
    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If we've already processed this vertex or found a shorter path, skip
        if current_vertex in processed or current_distance > distances[current_vertex]:
            continue
        
        # Mark the vertex as processed
        processed.add(current_vertex)
        
        # Process all neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            # Calculate the distance through the current vertex
            distance = current_distance + weight
            
            # If this path is shorter than the previously known path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

def get_shortest_path(predecessors, start, end):
    """
    Reconstruct the shortest path from start to end using the predecessors dictionary
    
    Args:
        predecessors: Dictionary with predecessor of each vertex
        start: Starting vertex
        end: Ending vertex
    
    Returns:
        path: List representing the shortest path from start to end
    """
    path = []
    current = end
    
    # If there's no path to the end vertex
    if predecessors[end] is None and start != end:
        return path
    
    # Reconstruct the path from end to start
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    # Reverse the path to get start to end
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
        # Comment out the line below for directed graphs
        # For undirected graphs, add the reverse edge
        # graph[v].append((u, weight))
    
    return graph

# Example usage
if __name__ == "__main__":
    # Example directed graph represented as a list of edges: (u, v, weight)
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 5),
        (1, 3, 10),
        (2, 3, 3),
        (2, 4, 2),
        (3, 4, 4),
        (3, 5, 11),
        (4, 5, 8)
    ]
    
    # Create the graph
    graph = create_graph_from_edges(edges)
    
    # Choose a start vertex
    start_vertex = 0
    
    # Find shortest paths
    start_time = time.time()
    distances, predecessors = dijkstra(graph, start_vertex)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Time taken for Dijkstra's algorithm: {elapsed_time:.6f} seconds")
    # Print shortest distances
    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"To vertex {vertex}: {distance}")
    
    # Print shortest paths
    print("\nShortest paths from vertex {start_vertex}:")
    for vertex in graph:
        if vertex != start_vertex:
            path = get_shortest_path(predecessors, start_vertex, vertex)
            print(f"To vertex {vertex}: {' -> '.join(map(str, path))}")