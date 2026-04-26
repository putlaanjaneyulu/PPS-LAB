Available_paintings = [
    "Starry Night",
    "The Mona Lisa",
    "The Last Supper",
    "The Scream",
    "Girl with a Pearl Earring"
]

want_to_buy = input("Enter the painting you want to buy: ")

if want_to_buy in Available_paintings:
    print(f'Yes, we have "{want_to_buy}" available for purchase!')
else:
    print(f'Sorry, we don\'t have "{want_to_buy}" right now.')
