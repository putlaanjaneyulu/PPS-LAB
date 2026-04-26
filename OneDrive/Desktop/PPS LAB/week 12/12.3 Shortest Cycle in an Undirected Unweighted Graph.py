from collections import deque
def shortest_cycle(n, graph):
    min_cycle = float('inf') 
    for start in range(n):
        dist = [-1] * n
        parent = [-1] * n    
        queue = deque()
        dist[start] = 0
        queue.append(start) 
        while queue:
            u = queue.popleft()    
            for v in graph[u]:
                # If not visited
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)  
                # If visited and not parent → cycle found
                elif parent[u] != v:
                    cycle_length = dist[u] + dist[v] + 1
                    min_cycle = min(min_cycle, cycle_length)
    return min_cycle if min_cycle != float('inf') else -1
# Example corresponding to cycle: 6 -> 1 -> 5 -> 0 -> 6


n = 5
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

result = shortest_cycle(n, graph)
print("Length of shortest cycle:", result)
