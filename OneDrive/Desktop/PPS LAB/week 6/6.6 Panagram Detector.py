
s = input("Enter a sentence: ")

a = set("abcdefghijklmnopqrstuvwxyz")

b = set(ch for ch in s.lower() if ch.isalpha())

if a.issubset(b):
    print("The sentence is a pangram")
else:
    print("The sentence is not a pangram")
