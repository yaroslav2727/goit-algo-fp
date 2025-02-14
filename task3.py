import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
                
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "C": 3, "D": 5},
    "C": {"B": 3, "D": 4, "A": 4},
    "D": {"C": 4, "E": 3, "G": 7},
    "E": {"D": 3, "G": 5, "H": 6},
    "G": {"E": 5, "H": 4, "K": 8},
    "H": {"G": 4, "J": 3, "L": 7},
    "J": {"H": 3, "K": 4, "M": 6},
    "K": {"J": 4, "L": 5, "N": 7},
    "L": {"K": 5, "M": 3, "O": 8},
    "M": {"L": 3, "N": 9, "O": 6},
    "N": {"M": 9, "O": 3, "K": 7},
    "O": {"N": 3, "L": 8, "M": 6}
}

print("Graph:", graph)
    
start_node = "K"
shortest_paths = dijkstra(graph, start_node)
    
print(f"Shortest paths from node {start_node}:")
for node, distance in shortest_paths.items():
    print(f"To {node}: {distance}")