

available = input("Enter the available currency: ").split(",")
to_order = input("Enter the currency to order: ").split(",")
requested = input("Enter the customer required currency: ").strip()

available = [currency.strip() for currency in available]
to_order = [currency.strip() for currency in to_order]

if requested in available:
    print("Yes,", requested, "are available.")
    available.remove(requested)
    to_order.append(requested)
else:
    print("NO, Currency is not available.")
    to_order.append(requested)

print("Updated available currencies:", available)
print("Updated currencies to order:", to_order)
