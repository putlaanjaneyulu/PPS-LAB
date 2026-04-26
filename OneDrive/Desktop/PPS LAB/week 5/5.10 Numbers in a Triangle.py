

while True:

    n = int(input("Enter a number: "))

    triangle_dict = {}


    for i in range(1, n + 1):
        triangle_dict[i] = [i] * i
        print(i, triangle_dict[i])


    choice = input("Do you want to play again? (y/n): ")

    if choice.lower() != 'y':
        print("Thank you for playing!")
        break
