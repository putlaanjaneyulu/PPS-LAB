def greedy_coloring(graph, V):
    result = [-1] * V
    result[0] = 0
    for u in range(1, V):
        used_colors = set()    
        for neighbor in graph[u]:
            if result[neighbor] != -1:
                used_colors.add(result[neighbor])
              # Find the first available color
        color = 0
        while color in used_colors:
            color += 1
        result[u] = color
    return result
V = 5
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4,],
    3: [1, 4],
    4: [2, 3]
}
colors = greedy_coloring(graph, V)
print("Vertex Assigned Color")
for vertex in range(V):
    print(vertex, colors[vertex])
print("Total colors used:", max(colors) + 1)
