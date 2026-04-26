shoes = input().split()
add_shoe = input().split()
remove_shoe = input().split()
requested_shoe = input().split()

if requested_shoe in shoes:
    shoes.remove(requested_shoe)

print(f"Final List of shoes:{shoes}")

if requested_shoe in shoes:
    print(f"Yes, {required_shoe} are available in the store.")

else:
    print(f"Sorry, {requested_shoe} are not available in the store.")
