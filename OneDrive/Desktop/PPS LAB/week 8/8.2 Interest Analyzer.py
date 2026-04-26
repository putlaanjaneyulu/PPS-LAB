def simple_interest(p, r, t):
    return (p * r * t) / 100
def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    return amount - p
P = int(input("Principal amount: "))
R = float(input("Rate of Interest: "))
T = int(input("Time period: "))
SI = simple_interest(P, R, T)
CI = compound_interest(P, R, T)
print(f"Simple Interest: {SI:.2f}")
print(f"Compound Interest: {CI:.2f}")
