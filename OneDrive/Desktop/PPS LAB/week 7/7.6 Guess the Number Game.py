import random
def playGame():
    number = random.randint(0, 100)
    attempts = 0
    print("I'm thinking of a number between 0 and 10...")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
playGame()
