# implicit set creation
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

# explicit ctor
wild_animals = set({"lion", "tiger", "panther"})

farm_animals.add("horse")
wild_animals.add("horse")

# empty braces creates empty dict
empty_set = set()

even = set(range(0, 40, 2))
print(even)  # these are UNORDERED

squares_tuple = (1, 4, 9, 16, 25)
squares = set(squares_tuple)
print(squares)

# elements that are in a or b
print(even.union(squares))  # same as squares.union(even)

print("-" * 40)

# elements that are in a and b
print(even.intersection(squares))
print(even & squares)

# elements that are in a but not b
print(sorted(even))
print(even.difference(squares))  # makes it clear you are working on a set
print(sorted(even - squares))  # infix operators can be confusing
print(squares - even)

# in place subtraction
even.difference_update(squares)
print(sorted(even))

# elements that are in either a or b but not both
print("symmetric even minus squares")
even = set(range(0, 40, 2))
print(even.symmetric_difference(squares))
print(squares.symmetric_difference(even))
print(even ^ squares)  # for some reason these print sorted

even.remove(2)  # use if you want the error to be raised on failure
even.discard(2)  # works even though 2 is not in set

# safe remove call
if 2 in even:
    even.remove(2)

# will be covered later
try:
    even.remove(2)  # fails
except KeyError:
    print("Not in set")

subset = {4, 6}
# these both print
if subset.issubset(even):
    print("sub")

if even.issuperset(subset):
    print("super")

# frozen sets are immutable, so can be used as dict keys

frozen = frozenset(range(0, 100, 2))
print(frozen)
frozen.add(2)  # fails with red squiggly
