# tuples are immutable sets of ordered items

# same
t1 = (1, 2)
t2 = 1, 2

print(t2)

# not same, parens needed to avoid syntactic ambiguty
print("a", "b", "c")  # a b c
print(("a", "b", "c"))  # ('a', 'b', 'c')

# useful for line splitting
t3 = (
    1,
    2,
    3
)

# different data types
welcome = "Welcome To My Nightmare", "Alice Cooper", 1975

print(welcome)
print(welcome[0])

# welcome[2] = 1976  # TypeError as immutable

# can update like so. RHS evaluated before LHS assignment
welcome = welcome[0], welcome[1], 1976

print(welcome)

welcome2 = [welcome[0], welcome[1], welcome[2]]
welcome2[2] = 1975  # works as lists mutable
print(welcome2)

# tuples good as dictionary key requires immutable object
# list intended to have same type (but not required), tuples not
# can also make sure things won't change after creation


# assignment primer
a = b = c = d = 12  # all 12
a, b = 12, 13
a, b = b, a  # swaps
print("a is {}".format(a))  # 13

# meaningful, named variables vs. a list
title, artist, year = welcome  # unpacking
print(title)
print(artist)
print(year)

title, artist, year = welcome2  # also works

# welcome2.append("Rock")
# title, artist, year = welcome2  # doesn't work when above called first

# welcome.append("Rock")
# fails here rather than during unpacking,
# also have red squiggly so helpful

# parens required
imelda = (
    "more Mayhem",
    "Imelda May",
    2011,
    ((1, "Track 1"), (2, "Track 2"))
)

_, _, _, tracks = imelda
print(tracks)

for number, title in tracks:
    print("\t{0}: {1}".format(number, title))

# tuple not fully immutable if it contains a mutable field e.g. list
tuple_with_list = 1, 2, ["a", "b"]
_, _, l = tuple_with_list
l.append("c")
print(tuple_with_list[2])  # includes 'c'
