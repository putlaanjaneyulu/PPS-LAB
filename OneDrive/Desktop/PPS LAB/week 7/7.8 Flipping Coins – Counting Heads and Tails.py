import random
def flip_coin(n):
    return [random.choice([True, False]) for _ in range(n)]
def count_results(flips):
    heads = flips.count(True)
    tails = flips.count(False)
    return heads, tails
def calculate_ratio(heads, tails):
    if tails == 0:
        return float('inf')  
    return heads / tails
flips_8 = flip_coin(8)
heads_8, tails_8 = count_results(flips_8)
ratio_8 = calculate_ratio(heads_8, tails_8)
flips_1000 = flip_coin(1000)
heads_1000, tails_1000 = count_results(flips_1000)
ratio_1000 = calculate_ratio(heads_1000, tails_1000)
print("Results for 8 flips:", flips_8)
print(f"Heads: {heads_8}, Tails: {tails_8}")
print(f"Ratio (Heads/Tails) for 8 flips: {ratio_8:.2f}")
print("\nResults for 1000 flips:")
print(f"Heads: {heads_1000}, Tails: {tails_1000}")
print(f"Ratio (Heads/Tails) for 1000 flips: {ratio_1000:.2f}")
print("\nComparison:")
if abs(ratio_1000 - 1) < abs(ratio_8 - 1):
    print("The ratio for 1000 flips is closer to 1,showing more balanced results.")
else:
    print("The ratio for 8 flips happened to be closer to 1 this time.")
