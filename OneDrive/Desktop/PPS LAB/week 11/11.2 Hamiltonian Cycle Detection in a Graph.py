# Function to check if current vertex can be added to Hamiltonian Cycle
def is_safe(v, graph, path, pos):
    # Check if this vertex is adjacent to previous vertex
    if graph[path[pos - 1]][v] == 0:
        return False
    # Check if vertex already included in path
    if v in path:
        return False
    return True
# Backtracking function to solve Hamiltonian Cycle
def hamiltonian_cycle_util(graph, path, pos):
    n = len(graph)
    # If all vertices are included
    if pos == n:
        # Check if last vertex connects to first
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    # Try different vertices as next candidate
    for v in range(1, n):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            # Backtrack
            path[pos] = -1
    return False
# Main function
def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n
    # Start at vertex 0
    path[0] = 0
    if not hamiltonian_cycle_util(graph, path, 1):
        print("No Hamiltonian Cycle exists.")
        return
    # Print cycle (include return to start)
    print("Hamiltonian Cycle exists:", path + [path[0]])
graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0]
]
hamiltonian_cycle(graph)
