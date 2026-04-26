n = int(input())

inventory = []

for i in range(n):
    item_name, price, quantity = input().split()
    inventory.append((item_name, int(price), int(quantity)))

m = int(input())

purchases = []

for i in range(m):
    item_name, qty = input().split()
    purchases.append((item_name, int(qty)))

total_bill = 0
updated_inventory = []

for item in inventory:
    name, price, stock_qty = item
    sold_qty = 0

    for purchase in purchases:
        if purchase[0] == name:
            if purchase[1] <= stock_qty:
                sold_qty = purchase[1]
                total_bill += price * sold_qty
            break

    updated_inventory.append((name, price, stock_qty - sold_qty))

print(f"Total Bill: {total_bill}")
print("Updated Inventory:")

for item in updated_inventory:
    print(item[0], item[1], item[2])
