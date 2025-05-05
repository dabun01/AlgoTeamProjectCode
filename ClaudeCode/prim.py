import heapq
import time

def prim_mst(graph):
    """
    Find the Minimum Spanning Tree of a graph using Prim's algorithm
    
    Args:
        graph: Dictionary representing an adjacency list with weights
              Format: {node: [(neighbor, weight), ...], ...}
    
    Returns:
        mst: List of edges in the MST
        total_weight: Total weight of the MST
    """
    # Start with any vertex (here we choose the first one)
    start_vertex = next(iter(graph))
    
    # Set to keep track of vertices in MST
    mst_set = {start_vertex}
    
    # List to store edges of MST
    mst = []
    
    # Priority queue to store edges
    # Format: (weight, current_vertex, next_vertex)
    priority_queue = []
    
    # Add all edges of the starting vertex to the priority queue
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(priority_queue, (weight, start_vertex, neighbor))
    
    total_weight = 0
    
    # Continue until MST includes all vertices
    while priority_queue and len(mst_set) < len(graph):
        # Get the edge with minimum weight
        weight, u, v = heapq.heappop(priority_queue)
        
        # If the next vertex is already in MST, skip this edge
        if v in mst_set:
            continue
        
        # Add the vertex to MST set
        mst_set.add(v)
        
        # Add the edge to MST
        mst.append((u, v, weight))
        total_weight += weight
        
        # Add all edges from the newly added vertex
        for neighbor, edge_weight in graph[v]:
            if neighbor not in mst_set:
                heapq.heappush(priority_queue, (edge_weight, v, neighbor))
    
    return mst, total_weight

# Helper function to convert edge list to adjacency list
def edges_to_adjacency_list(edges, vertices):
    """
    Convert a list of edges to an adjacency list
    
    Args:
        edges: List of edges in the format (u, v, weight)
        vertices: Set of all vertices in the graph
    
    Returns:
        graph: Dictionary representing an adjacency list with weights
    """
    graph = {v: [] for v in vertices}
    
    for u, v, weight in edges:
        # For undirected graph, add edges in both directions
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    
    return graph

# Example usage
if __name__ == "__main__":
    # Example graph represented as a list of edges: (u, v, weight)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    # Set of all vertices
    vertices = {0, 1, 2, 3}
    
    # Convert to adjacency list
    graph = edges_to_adjacency_list(edges, vertices)
    
    # Find MST using Prim's algorithm
    start_time = time.time()
    mst, total_weight = prim_mst(graph)
    end_time = time.time()
    elapsed_time = end_time - start_time
    # Print the MST
    print("Edges in the Minimum Spanning Tree (Prim's):")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
    
    print(f"Total weight of MST: {total_weight}")
    print(f"Time taken for Prim's algorithm: {elapsed_time:.6f} seconds")