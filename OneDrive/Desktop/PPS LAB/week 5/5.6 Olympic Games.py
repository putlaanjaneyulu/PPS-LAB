
olympic_sports = {}


olympic_sports["Summer"] = ["Swimming", "Athletics"]
olympic_sports["Winter"] = ["Skiing", "Ice Hockey"]

olympic_sports["Summer"].append("Gymnastics")
olympic_sports["Winter"].append("Snowboarding")


olympic_sports["Summer"] += ["Cycling"]
olympic_sports["Winter"] += ["Figure Skating"]

print("Olympic Sports Dictionary:")
print("{'Summer':", olympic_sports["Summer"], ",")
print("'Winter':", olympic_sports["Winter"], "}")
print()


print("--- Printing items (method 1: using .items()) ---")
for season, sports in olympic_sports.items():
    print("Season:", season, "-> Sports:", sports)


print("--- Printing items (method 2: using keys) ---")
for season in olympic_sports:
    print("Season:", season, "-> Sports:", olympic_sports[season])


print("--- Only sports lists ---")
for sports in olympic_sports.values():
    print(sports)
