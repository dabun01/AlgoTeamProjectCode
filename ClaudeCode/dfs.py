from collections import defaultdict
import time

class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # A recursive function for DFS traversal
    def dfs_recursive(self, vertex, visited, result):
        # Mark the current vertex as visited
        visited.add(vertex)
        result.append(vertex)
        
        # Recur for all adjacent vertices
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)
    
    # DFS traversal using recursive approach
    def dfs(self, start_vertex):
        # Set to keep track of visited vertices
        visited = set()
        
        # List to store the DFS traversal result
        result = []
        
        # Call the recursive helper function
        self.dfs_recursive(start_vertex, visited, result)
        
        return result
    
    # DFS traversal using iterative approach (with stack)
    def dfs_iterative(self, start_vertex):
        # Set to keep track of visited vertices
        visited = set()
        
        # Stack for DFS
        stack = [start_vertex]
        
        # List to store the DFS traversal result
        result = []
        
        while stack:
            # Pop a vertex from the stack
            vertex = stack.pop()
            
            # If not visited, mark it as visited and add to result
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Push all adjacent vertices in reverse order
                # This ensures the original order of neighbors is preserved in the traversal
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    # Measure the time taken for DFS traversal
    print("DFS traversal (recursive) starting from vertex 2:")
    start_time = time.time()
    print(g.dfs(2))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for DFS (recursive): {elapsed_time:.6f} seconds")
    
    print("DFS traversal (iterative) starting from vertex 2:")
    start_time = time.time()
    print(g.dfs_iterative(2))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for DFS (iterative): {elapsed_time:.6f} seconds")