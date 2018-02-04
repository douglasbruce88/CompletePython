# update and copy
fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, lemon citrus fruit",
    "grape": "a small, sweet fruit growing in bunches"}

veg = {
    "cabbage": "every childs's favourite",
    "sprouts": "mmm, lovely",
    "spinach": "can I have soem more fruit, please?"}

veg.update(fruit)  # returns none
print(veg)
print(fruit)  # still the same as above

# new dict containing both without modifying originals
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
