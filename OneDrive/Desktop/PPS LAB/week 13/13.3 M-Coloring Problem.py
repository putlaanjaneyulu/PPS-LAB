def is_safe(v, graph, color, c, V):
    for i in range(V):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def solve_m_coloring(graph, m, color, v, V):
    # If all vertices are assigned a color
    if v == V:
        return True

    # Try different colors
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c, V):
            color[v] = c

            if solve_m_coloring(graph, m, color, v + 1, V):
                return True

            # Backtrack
            color[v] = 0

    return False


def graph_coloring(graph, m):
    V = len(graph)
    color = [0] * V

    if not solve_m_coloring(graph, m, color, 0, V):
        print("Solution does not exist")
        return False

    print("Solution Exists: Following are the assigned colors:")
    for c in color:
        print(c, end=" ")
    return True


# ------------------ Sample Test Case 1 ------------------
graph1 = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]


m = 3
graph_coloring(graph1, m)

print("\n")
"""
# ------------------ Sample Test Case 2 ------------------
graph1 = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
graph_coloring(graph2, m)
"""