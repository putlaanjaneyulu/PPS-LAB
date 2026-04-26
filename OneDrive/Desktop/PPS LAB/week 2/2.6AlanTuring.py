alan_turing = [ "Turing", "created", "an electromechanical machine",
    "to crack","the Nazi Navy's","Enigma Code"]

method_list = alan_turing[:]

method_list[4] = "Enigma Code"

method_list[3] = "shortened the war"

method_list.insert(5, "by two years")

method_list[2] = "his contribution"


method_list.append("saving millions of lives")

method_list[1] = "that"

method_list.remove("to crack")

method_list[0] = "It is estimated"


method_list.pop(5)
print("After operations using list slicing:")

print(method_list)


