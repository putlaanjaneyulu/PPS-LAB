import heapq
def dijkstra(V, graph, source):
    dist = [float('inf')] * V
    dist[source] = 0
 # Min-heap priority queue (distance, vertex)
    pq = [(0, source)] 
    while pq:
        current_dist, u = heapq.heappop(pq) 
        # If we already found a better path, skip
        if current_dist > dist[u]:
            continue
        # Explore neighbors
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist
V = 4
graph = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 6)],
    2: [(0, 4), (1, 2), (3, 3)],
    3: [(1, 6), (2, 3)]
}
source = 0
distances = dijkstra(V, graph, source)
print("Vertex Distance from Source")
for i in range(V):
    print(f"  {i},           {distances[i]}")
