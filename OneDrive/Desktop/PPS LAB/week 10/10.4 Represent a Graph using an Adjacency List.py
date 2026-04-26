n =int(input("Number of vertices: "))
edges = [(0, 1), (2, 1), (3, 2)]
adj_list = {i: [] for i in range(n)}
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u) 
print("Adjacency List:")
for vertex in adj_list:
    print(f"{vertex}: {adj_list[vertex]}")




'''

output

4
Adjacency List:
0: [1]
1: [0, 2]
2: [1, 3]
3: [2]


'''
