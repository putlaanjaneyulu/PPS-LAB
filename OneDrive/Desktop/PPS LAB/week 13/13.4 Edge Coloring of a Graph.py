def edge_coloring(edges):
    edge_colors = {}
    for i in range(len(edges)):
        u1, v1 = edges[i]
        used_colors = set()  
        for j in range(i):
            u2, v2 = edges[j] 
            # Check if edges are adjacent (share a vertex)
            if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
                used_colors.add(edge_colors[j])
        color = 1
        while color in used_colors:
            color += 1 
        edge_colors[i] = color
    return edge_colors
edges = [
    (1, 4),  
    (1, 2),
    (1, 3),  
    (3, 2)   
]
result = edge_coloring(edges)
for i in range(len(edges)):
    print(f"Edge {i+1} is of color {result[i]}")
