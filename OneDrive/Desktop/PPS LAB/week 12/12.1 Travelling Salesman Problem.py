import itertools
def tsp(graph):
    n = len(graph)
    cities = list(range(n))    
    min_cost = float('inf')
    best_path = []    
    for perm in itertools.permutations(cities[1:]):
        current_cost = 0
        current_path = [0] + list(perm) + [0]   
        # Calculate cost of the current path
        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i+1]]
        # Update minimum cost and best path
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path   
    return min_cost, best_path

graph = [
 [0, 12, 10, 19],
 [12, 0, 3, 7],
 [10, 3, 0, 6],
 [19, 7, 6, 0]

]
min_cost, path = tsp(graph)
print("Minimum tour cost:", min_cost)
print("Optimal path:", path)
