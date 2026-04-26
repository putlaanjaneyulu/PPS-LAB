graph = {
    0: [1, 2],
    1: [0, 2],
    2: [2, 1, 3],
    3: [2],
    4: [1, 2],
}
print(graph)
total = 0
for vertex in graph:
    total += len(graph[vertex])
edges = total // 2
print("Total number of edges:", edges)


'''
out put
Total number of edges: 5

'''
