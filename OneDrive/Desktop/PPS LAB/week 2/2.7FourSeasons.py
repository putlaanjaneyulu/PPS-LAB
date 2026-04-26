seasons = ["spring", "summer", "fall", "winter"]
print("Seasons with at least 5 characters: ")
for season in seasons:
    if len(season) >= 5:
        print(season)
print("Seasons with 4 or fewer characters: ")
for season in seasons:
    if len(season) <= 4:
        print(season)
print("Seasons with index less than 2: ")
for i in range(len(seasons)):
    if i < 2:
        print(seasons[i])
print("Seasons with index at least 2: ")
for i in range(len(seasons)):
    if i >= 2:
        print(seasons[i])


