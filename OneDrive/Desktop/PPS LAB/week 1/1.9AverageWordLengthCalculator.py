sentence = input("Sentence: ")
words = sentence.split()
total = 0
for word in words:
    total += len(word)

average = total / len(words)

print("Average word length:", average)
