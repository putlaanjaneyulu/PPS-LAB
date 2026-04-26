
colosseum = {
    "Location": "Rome",
    "Construction Years": "70–80 AD",
    "Type": "Amphitheater"
}

print("Initial Colosseum Information:")
print(colosseum)


colosseum.pop("Construction Years")


colosseum["Construction Start Year"] = 72


colosseum.update({"Construction End Year": 80})

print("\nAfter Updating Construction Details:")
print(colosseum)

start_year = colosseum["Construction Start Year"]
end_year = colosseum["Construction End Year"]

years_taken = end_year - start_year
print("\nYears taken to build the Colosseum:", years_taken)


current_year = 2025
years_passed = current_year - start_year
print("Years passed since construction began:", years_passed)
