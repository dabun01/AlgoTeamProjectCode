# Implementation of Kruskal's algorithm for finding Minimum Spanning Tree
import time
class DisjointSet:
    def __init__(self, vertices):
        # Initialize each vertex as a separate set with itself as parent
        self.parent = {v: v for v in vertices}
        # Initialize rank of each vertex as 0
        self.rank = {v: 0 for v in vertices}
    
    # Find the parent of a vertex with path compression
    def find(self, item):
        # If item is not the parent of itself, then find its parent
        if self.parent[item] != item:
            # Path compression: make the parent of item to be the root parent
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    # Union of two sets by rank
    def union(self, x, y):
        # Find the root parents
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If they are already in the same set
        if root_x == root_y:
            return
        
        # Attach the smaller rank tree under the root of the higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are same, make one as root and increment its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

def kruskal_mst(graph, vertices):
    """
    Find the Minimum Spanning Tree of a graph using Kruskal's algorithm
    
    Args:
        graph: List of edges in the format (u, v, weight)
        vertices: Set of all vertices in the graph
    
    Returns:
        result: List of edges in the MST
    """
    # Sort all edges in non-decreasing order of their weight
    graph.sort(key=lambda x: x[2])
    
    # Initialize result
    result = []
    
    # Create disjoint sets for each vertex
    ds = DisjointSet(vertices)
    
    # Number of edges to be taken is equal to V-1
    edge_count = 0
    i = 0
    
    # While edge_count is less than V-1
    while edge_count < len(vertices) - 1:
        # If we've checked all edges and still haven't found V-1 edges for MST
        if i >= len(graph):
            break
            
        # Get the smallest edge
        u, v, w = graph[i]
        i += 1
        
        # Check if including this edge creates a cycle
        set_u = ds.find(u)
        set_v = ds.find(v)
        
        # If including this edge doesn't cause a cycle, include it in result
        if set_u != set_v:
            edge_count += 1
            result.append((u, v, w))
            ds.union(set_u, set_v)
    
    return result

# Example usage
if __name__ == "__main__":
    # Example graph represented as a list of edges: (u, v, weight)
    graph = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    # Set of all vertices
    vertices = {0, 1, 2, 3}
    
    # Find MST
    start_time = time.time()
    mst = kruskal_mst(graph, vertices)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print the MST
    print("Edges in the Minimum Spanning Tree:")
    total_weight = 0
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
        total_weight += weight
    
    print(f"Total weight of MST: {total_weight}")
    print(f"Time taken for Kruskal's algorithm: {elapsed_time:.6f} seconds")