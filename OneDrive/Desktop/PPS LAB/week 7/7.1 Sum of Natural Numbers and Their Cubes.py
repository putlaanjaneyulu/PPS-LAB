def sumN(n):
    return n * (n + 1) // 2
def sumNCubes(n):
    return (n*(n+ 1) // 2) ** 2
n = int(input("Enter a number"))

print(f"Sum of first {n} natural numbers: {sumN(n)}")
print(f"Sum of cubes of first {n} natural numbers: {sumNCubes(n)}")
