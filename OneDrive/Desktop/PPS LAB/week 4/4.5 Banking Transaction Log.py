
n = int(input())
if n == 0:
    print("No transactions found.")
else:
    balances = {}
    
    for _ in range(n):
        account_number, transaction_type, amount = input().split()
        account_number = int(account_number)
        amount = float(amount)

        if account_number not in balances:
            balances[account_number] = 0
            

        if transaction_type == "credit":
            balances[account_number] += amount
            
        elif transaction_type == "debit":
            balances[account_number] -= amount
            
    for account, balance in balances.items():
        print((account, balance))


        