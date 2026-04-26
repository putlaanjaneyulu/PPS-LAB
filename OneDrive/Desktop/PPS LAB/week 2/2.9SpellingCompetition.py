msk_words = [
    "ankle", "patella", "rib", "femur", "sternocleidomastoid",
    "tendon", "sternum", "abdominal external oblique", "muscle",
    "scapula", "radius", "bone", "vertebra", "ligament",
    "ulna", "skull", "clavicle" ]


print(f"Total number of words to learn: {len(msk_words)}")

print("Length of each word:")


for word in msk_words:
    print(f"{word}: {len(word)}")



short = ["leg"]
for word in msk_words:
    if len(word) <= 6:
        short.append(word)




print(f"Short words (6 or fewer characters): {short}")
print(f"Number of short words: {len(short)}")




intermediate = ["cartilage"]
for word in msk_words:
    if 7 <= len(word) <= 9:
        intermediate.append(word)



print(f"Intermediate words (7–9 characters): {intermediate}")
print(f"Number of intermediate words: {len(intermediate)}")



long = ["pectoralis major"]
for word in msk_words:
    if len(word) >= 10:
        long.append(word)

        

print(f"Long words (10+ characters): {long}")
print(f"Number of long words: {len(long)}")
