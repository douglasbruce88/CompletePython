locations = {
    0: {"desc": "computer",
        "exits": {},
        "namedExits":  {}},
    1: {"desc": "road",
        "exits": {"W": 2, "E": 3},
        "namedExits": {"2": 2, "3": 3}},
    2: {"desc": "hill",
        "exits": {"N": 5, "Q": 0},
        "namedExits": {"5": 5}}}

vocabulary = {
    "QUIT": "Q",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3"}

loc = 1
while True:
    # don't need .keys() here, why not?
    availableExits = ", ".join(locations[loc]["exits"])
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()

    if len(direction) > 1:
        for word in direction.split():
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")
