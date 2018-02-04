# dicts accessed by key rather than index, no duplicates allowed
# if duplicates on assignment, last entry wins but you can a warning
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, lemon citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "apple": "round and crunchy"}

print(fruit)
print(fruit["apple"])

# no method to add/insert, just an indexer
fruit["pear"] = "an odd shaped apple"
print(fruit["pear"])
fruit["lemon"] = "great with tequila"  # overwrites entry
print(fruit["lemon"])

del fruit["lemon"]  # removes but del is very powerful so take care
print(fruit)

fruit.clear()  # removes all entries (del fruit would delete whole thing)

# returns description if present else default val
print(fruit.get("lemon", "default val"))

# another way to check existence
if "lemon" in fruit:
    print(fruit["lemon"])

# KeyError fruit["lemon"]

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, lemon citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "apple": "round and crunchy"}


# iterate over keys. ordering is *random* at creation time
# adding/removing is also unordered
for snack in fruit:
    print(fruit[snack])

# if ordering important, can create list of keys,
# sort list and iterate over them
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + " - " + fruit[f])

# concise alternative
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# less efficient than using keys
for val in fruit.values():
    print(val)

# 'view object' that cannot be added to directly
# but can be modified behind the scenes
fruit_keys = fruit.keys()
fruit["tomato"] = "Not nice with ice cream"
print(fruit_keys)  # includes tomato

print(fruit.items())  # set-like view object containing tuples
print(tuple(fruit.items()))  # regular tuple

for snack in fruit.items():
    item, description = snack
    print(item + " is " + description)

# can go the other way as well
print(dict(fruit.items()))
