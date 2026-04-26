def evaluate_loan(annual_income, credit_score, existing_loan):
    # Determine loan status
    if credit_score >= 750 and annual_income >= 500000:
        status = "Loan Approved"
    elif 650 <= credit_score <= 749 and annual_income >= 300000 and existing_loan <= 200000:
        status = "Loan Conditionally Approved"
    else:
        status = "Loan Rejected"
    max_loan = annual_income * 0.5
    return status, max_loan
annual_income = int(input("amt:"))
credit_score = int(input("score:"))
existing_loan = int(input("exloan:"))
status, max_loan = evaluate_loan(annual_income, credit_score, existing_loan)
print(status)
print(f"Maximum Eligible Loan: ₹{max_loan:.2f}")
