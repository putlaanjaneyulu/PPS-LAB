numbers = [7, 9, 15, 19, 24, 30, 37, 45, 50]
def divisible_by_both(nums):
    result = [n for n in nums if n % 3 == 0 and n % 5 == 0]
    print("Numbers divisible by both 3 and 5:", result)
def divisible_by_either(nums):
    result = [n for n in nums if n % 3 == 0 or n % 5 == 0]
    print("Numbers divisible by 3 or 5:", result)
def divisible_by_3_not_5_using_not(nums):
    result = [n for n in nums if n % 3 == 0 and not n % 5 == 0]
    print("Numbers divisible by 3 but not 5 (using not):", result)
def divisible_by_3_not_5_without_not(nums):
    result = [n for n in nums if n % 3 == 0 and n % 5 != 0]
    print("Numbers divisible by 3 but not 5 (without using not):", result)
divisible_by_both(numbers)
divisible_by_either(numbers)
divisible_by_3_not_5_using_not(numbers)
divisible_by_3_not_5_without_not(numbers)
