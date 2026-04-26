n =int(input("Number of vertices:"))
edges = [(0, 1), (1, 2),(1,3)]
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
for u, v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1   
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

'''
 output

 Number of vertices:4
Adjacency Matrix:
[0, 1, 0, 0]
[1, 0, 1, 1]
[0, 1, 0, 0]
[0, 1, 0, 0]

'''
