locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "Hill",
    3: "Well house",
    4: "Valley",
    5: "Forest"}

# challenge: change exits to a dictionary
exits = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}}

# challenge: create dict of words which player may use
words = {
    "W": "W",
    "WEST": "W",
    "GO WEST": "W"}  # etc

"a b c".split()
"a, b, c".split(",")

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()

    if len(direction) > 1:
        for word in direction.split():
            if word in words.keys():
                direction = words[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
