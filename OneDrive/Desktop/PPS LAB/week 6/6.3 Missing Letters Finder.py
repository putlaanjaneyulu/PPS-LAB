word1=input("enter word1:")
word2=input("enter word2:")
word1=word1.lower()
word2=word2.lower()

set1 = set(word1)
set2 = set(word2)
alphabets={"abcdefghijklmnopqrstuvwxyz"}

present_letters = set1.union(set2)


missing_letters = alphabets.difference(present_letters)


print("Letters not present in either word:")
print(" ".join(sorted(missing_letters)))
    
