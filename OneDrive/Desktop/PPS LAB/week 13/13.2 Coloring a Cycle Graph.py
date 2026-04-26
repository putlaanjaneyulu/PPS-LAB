def cycle_graph_coloring(vertices):
    if vertices % 2 == 0:
        return 2
    else:
        return 3


# Sample Inputs
vertices = 5
print("No. of colors require is:", cycle_graph_coloring(vertices))

vertices = 6

print("No. of colors require is:", cycle_graph_coloring(vertices))
