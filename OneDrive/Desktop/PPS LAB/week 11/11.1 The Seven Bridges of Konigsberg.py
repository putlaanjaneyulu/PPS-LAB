graph = {
    'P': ['Q', 'R', 'S'],
    'Q': ['P', 'R', 'S'],
    'R': ['P', 'Q'],
    'S': ['P', 'Q']
}
print("Degrees of vertices:")
odd_count = 0
for vertex in graph:
    degree = len(graph[vertex])
    print(f"{vertex}: {degree}")
    if degree % 2 != 0:
        odd_count += 1
if odd_count == 0:
    print("Result: The graph has an Eulerian Circuit(can return to start).")
elif odd_count == 2:
    print("Result: The graph has an Eulerian Path (cannot return to start).")
else:
    print("Result: The graph is not Eulerian(no Euler path or circuit).")

'''
OUT PUT

CASE 2
Degrees of vertices:
P: 3
Q: 3
R: 2
S: 2
'''
