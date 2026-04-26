sentence = input()
words = sentence.split()

acronym = " "

for word in words :
    acronym += word[0].upper()

print(acronym)


