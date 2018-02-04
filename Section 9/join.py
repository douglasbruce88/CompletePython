# strings mutable so concat not efficient, use join instead
my_list = ["a", "b", "c", "d"]
letters = "abcde"

# bad
newString = ""
for c in my_list:
    newString += c + ", "

# good
print(", ".join(my_list))
print(", ".join(letters))

locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "Hill",
    3: "Well house",
    4: "Valley",
    5: "Forest"}

# list of dictionaries. looks odd to me
exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
