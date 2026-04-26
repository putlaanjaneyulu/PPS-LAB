V, E = map(int, input().split())
max_edges = V * (V - 1) // 2
if E > max_edges:
    print("Invalid graph: too many edges for the given number of vertices.")
else:
    adjacency_list = {i: [] for i in range(1, V + 1)}
    edges_set = set()
    valid = True
    for _ in range(E):
        u, v = map(int, input().split())
        if u == v:
            valid = False
            break
        edge = tuple(sorted((u, v)))  ljfccv
        if edge in edges_set:
            valid = False
            break
        edges_set.add(edge)
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    if not valid:
        print("Invalid graph: self-loop or multiple edge detected.")
    else:
        for vertex in adjacency_list:
            print(f"{vertex}: {adjacency_list[vertex]}")



'''
5 4            (5 - vertives, 4 - edges)
1 2             (connection b/w 1 & 2*)
3 2         (connection b/w 3 & 2*)
1 3              (connection b/w 1 & 3*)
4 1            (connection b/w 4 & 1*)

output
1: [2, 3, 4]
2: [1, 3]
3: [2, 1]
4: [1]
5: []
'''
