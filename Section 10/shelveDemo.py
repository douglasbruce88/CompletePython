# shelve good if you don't want to read things
# entirely into memory before pickling them

# shelf is a dict with string key and picklable val
# calling file needs to be called something other than shelve.py
import shelve

# creates bak, dat and dir files i.e. a database
with shelve.open(".\\Section 10\\ShelfTest") as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['lemon'] = "a sour, yellow cirtus fruit"
    print(fruit['lemon'])
    # this will overwrite the previous value
    fruit['lemon'] = "nice with vodka"

# this gives a ValueError as invalid op on a closed shelf
# can manually call open and .close() if more control required
# print(fruit['lemon'])

# not a dictionary, so can't create a shelf with a literal statement
print(fruit)

with shelve.open(".\\Section 10\\ShelfTest") as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['lemn'] = "a sour, yellow cirtus fruit"
    # shelves persist so we can end up with undesired keys from typos
    print(fruit['lemon'])
    print(fruit['lemn'])
    # can remove though!
    del fruit['lemn']
    # print(fruit['lemn'])  # now doesn't work, KeyError

# shelf is unordered so need to sort keys first
fruit = shelve.open(".\\Section 10\\ShelfTest")
ordered_keys = sorted(list(fruit.keys()))

for f in ordered_keys:
    print(f + ": " + fruit[f])

print(fruit.values())  # ValuesView, no details printed

for f in fruit.items():
    print(f)  # List of tuples

print(fruit.items())  # ItemsView, no details printed
fruit.close()

# overall a shelf acts a bit like a dictionary, but keys must be strings
