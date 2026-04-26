def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
def is_digit_power_sum(n):
    digit_sum = sum_of_digits(n)
    # A digit sum of 0 or 1 cannot form valid powers (except trivial case 1)
    if digit_sum <= 1:
        return False, digit_sum, None
    power = 1
    while digit_sum ** power <= n:
        if digit_sum ** power == n:
            return True, digit_sum, power
        power += 1
    return False, digit_sum, None
# Input
n = int(input())
# Check
result, digit_sum, power = is_digit_power_sum(n)
# Output
if result:
    print(f"{n} is a Digit Power Sum Number.")
    print(f"Sum of digits = {digit_sum}")
    print(f"{digit_sum}^{power} = {n}")
else:
    print(f"{n} is NOT a Digit Power Sum Number.")
