vowels = {'a', 'e', 'i', 'o', 'u'}

word = input("Enter an English word: ")
word_lower = word.lower()
count = 0
for char in word_lower:
    if char in vowels:
        count += 1

print(f"The word '{word}' contains {count} vowel(s).")
