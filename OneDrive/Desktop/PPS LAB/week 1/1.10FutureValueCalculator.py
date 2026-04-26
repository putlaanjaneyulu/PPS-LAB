amount = float(input("Enter the amount: "))
interest = float(input("Enter the rate of interest in decimal: "))
time = int(input("Enter time in years(no.of years): "))

print("Year     Value")
print("---------------")

for year in range(time + 1):
    value = amount * (1 + interest) ** year
    print(f"{year}      ${value:.2f}")
