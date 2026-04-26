
def floyd_warshall(graph, V):
    dist = [row[:] for row in graph]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist





"""
V = 5



graph = [
        [0, 4, INF, 5, INF],
        [INF, 0, 1, INF, 6],
        [2, INF, 0, 3, INF],
        [INF, INF, 1, 0, 2],
        [1, INF, INF, 4, 0]


]

"""
V = 1
INF = 99999
graph = [
    [0, 4, 11],
    [INF, 0, 2],
    [INF, INF, 0]
]

shortest_distances = floyd_warshall(graph, V)
print("Shortest distances between every pair of vertices:")
for row in shortest_distances:
    print(row)
