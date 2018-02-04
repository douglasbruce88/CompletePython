# load data from shelves
import shelve

locations = shelve.open(".\\Section 10\\locations")
vocabulary = shelve.open(".\\Section 10\\vocabulary")

loc = "1"
while True:
    # don't need .keys() here, why not?
    availableExits = ", ".join(locations[loc]["exits"])
    print(locations[loc]["desc"])

    if loc == "0":
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
        loc = str(allExits[direction])
    else:
        print("You cannot go in that direction")

locations.close()
vocabulary.close()
