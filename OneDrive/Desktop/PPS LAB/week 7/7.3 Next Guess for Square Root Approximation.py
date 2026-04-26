def nextGuess(guess, x):
    return 0.5 * (guess + x / guess)
guess = float(input("Enter a number "))
x = float(input("Enter a number"))
result = nextGuess(guess, x)
print(f"Next guess: {result:.2f}")
