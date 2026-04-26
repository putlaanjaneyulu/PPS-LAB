def grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"
score = float(input("Enter the score"))
result = grade(score)
if result == "Invalid":
    print("Invalid score")
else:
    print(f"Grade: {result}")
