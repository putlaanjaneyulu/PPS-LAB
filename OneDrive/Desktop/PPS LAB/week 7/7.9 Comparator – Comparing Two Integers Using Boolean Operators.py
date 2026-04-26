def compare_numbers(a, b):
    print(f"\nComparing {a} and {b}:")
    print(f"{a} > {b}  : {a > b}")
    print(f"{a} < {b}  : {a < b}")
    print(f"{a} >= {b} : {a >= b}")
    print(f"{a} <= {b} : {a <= b}")
    print(f"{a} == {b} : {a == b}")
    print(f"{a} != {b} : {a != b}")
def main():
    while True:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        compare_numbers(num1, num2)
        choice = input("\nDo you want to compare another pair? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Program ended.")
            break
main()
