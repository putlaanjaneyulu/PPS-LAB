import string

p1 = input("Enter first article: ")
p2 = input("Enter second article: ")

def clean_text(text):
    text = text.lower()  
 
    for ch in string.punctuation:
        text = text.replace(ch, "")

    return set(text.split())


set1 = clean_text(p1)
set2 = clean_text(p2)


common_words = set1.intersection(set2)
unique1 = set1.difference(set2)
unique2 = set2.difference(set1)
total_distinct = set1.union(set2)


print("Words common to both:", common_words)
print("Words unique to first article:", unique1)
print("Words unique to second article:", unique2)
print("Total distinct words in both articles:", len(total_distinct))
