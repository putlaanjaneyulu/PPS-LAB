


def count_sink_nodes(n, edges):
    out_degree = {i: 0 for i in range(1, n + 1)}
    print(out_degree)
    for u, v in edges:
        out_degree[u] += 1
        print(out_degree)
    sink_count = sum(1 for node in out_degree if
                     out_degree[node] == 0) 
    return sink_count
n, m = map(int, input("Enter number of nodes and edges: ").split())
edges = []
for _ in range(m):
    u, v = map(int, input("Enter edge (from to): ").split())
    edges.append((u, v))
print("Number of sink nodes:", count_sink_nodes(n, edges))
# #second method
n, m = map(int, input().split())
outdegree = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    outdegree[u] += 1  
sink_count = 0
for i in range(1, n + 1):
    if outdegree[i] == 0:
        sink_count += 1
print(sink_count)



# out put
'''
Enter number of nodes and edges: 4 3
Enter edge (from to): 1 2
Enter edge (from to): 2 3
Enter edge (from to): 1 4
{1: 0, 2: 0, 3: 0, 4: 0}
{1: 1, 2: 0, 3: 0, 4: 0}
{1: 1, 2: 1, 3: 0, 4: 0}
{1: 2, 2: 1, 3: 0, 4: 0}
Number of sink nodes: 2   '''
