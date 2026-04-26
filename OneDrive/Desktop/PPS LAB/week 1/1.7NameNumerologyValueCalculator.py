name = input()
total_value = 0

for ch in name:
    if 'A' <= ch <= 'Z':
        total_value += ord(ch) - ord('A') + 1
    elif 'a' <= ch <= 'z':
        total_value += ord(ch) - ord('a') + 1
print(total_value)
