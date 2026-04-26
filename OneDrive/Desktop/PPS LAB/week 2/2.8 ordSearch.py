words = ["cards", "park", "pets", "football", "golf", "crosswords", "toys", "exercise", "hobbies", "riding", 
            "biking", "games", "reading", "movies", "walking", "concerts"]




title = len(words)
print(f"Word search with {title} words.\n")

five_letter_words = []
for word in words:
    if len(word) == 5:
        five_letter_words.append(word)

        

print(f"Words with exactly 5 letters (Count: {len(five_letter_words)}):")
for word in five_letter_words:
    print(word)

    
print("Words with fewer than 5 characters:")
for index, word in enumerate(words):
    if len(word) < 5:
        print(f"'{word}' is at position {index} and has length {len(word)}.")



print("Words with more than 8 characters:")
for index, word in enumerate(words):
    if len(word) > 8:
        print(f"'{word}' is at position {index} and has length {len(word)}.")


second_half = words[len(words)//2:]
print("From the second half, words with length different from 7:")
for index, word in enumerate(second_half, start=len(words)//2):
    if len(word) != 7:
        print(f"'{word}' is at position {index} and has length {len(word)}.")




first_fourth = words[:len(words)//4]
print("From the first fourth, 4-letter words:")
for index, word in enumerate(first_fourth):
    if len(word) == 4:
        print(f"'{word}' is at position {index}.")
        
