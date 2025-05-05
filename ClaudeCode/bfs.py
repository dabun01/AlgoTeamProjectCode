from collections import defaultdict, deque
import time

class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # Function for BFS traversal
    def bfs(self, start_vertex):
        # Create a set for visited vertices
        visited = set()
        
        # Create a queue for BFS
        queue = deque([start_vertex])
        
        # Mark the start vertex as visited
        visited.add(start_vertex)
        
        # List to store the BFS traversal result
        result = []
        
        while queue:
            # Dequeue a vertex from the queue
            current_vertex = queue.popleft()
            result.append(current_vertex)
            
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it
            # visited and enqueue it
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
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

    # draw the graph
    
    print("BFS traversal starting from vertex 2:")
    # Measure the time taken for BFS traversal
    start_time = time.time()
    print(g.bfs(2))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for BFS traversal: {elapsed_time:.6f} seconds")