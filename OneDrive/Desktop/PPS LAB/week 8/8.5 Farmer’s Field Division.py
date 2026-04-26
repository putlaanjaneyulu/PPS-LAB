def number_of_plots(length, width, side):
    return (length // side) * (width // side)
def remaining_area(length, width, side):
    plots = number_of_plots(length, width, side)
    return (length * width) - (plots * side * side)
length = int(input())
width = int(input())
side = int(input())
plots = number_of_plots(length, width, side)
unused = remaining_area(length, width, side)
print(f"Number of plots: {plots}")
print(f"Remaining area: {unused} sq.m")
