import heapq

def find_shortest_path(graph, start, end):
    # Mesafeleri sonsuz yap
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Öncelik kuyruğu: (mesafe, düğüm)
    pq = [(0, start)]
    previous_nodes = {node: None for node in graph}
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue
        
        if current_node in graph:
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
    
    path = []
    current = end
    
    if distances[end] == float('infinity'):
        return None, 0

    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
        
    return path, distances[end]