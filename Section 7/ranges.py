print(range(100))  # starts at 0

my_list = list(range(10))
print(my_list)  # 0 to 9

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)  # 0, 2, 4, 6, 8
print(odd)  # 1, 3, 5, 7, 9

# same amount of memory
range(0, 10)
range(0, 10000000)

# lots of memory
list(range(0, 10000))

# ranges don't support * for repeating or append/+

my_string = "abcdef"
print(my_string.index('e'))  # 4
print(my_string[4])  # e

small_decimals = range(10)
print(small_decimals.index(3))  # 3
odd = range(1, 10000, 2)
print(odd[985])  # 1971

sevens = range(7, 1000000, 7)
x = 49
if x in sevens:
    print("{} is div by 7".format(x))

my_range = small_decimals[::2]
print(my_range)  # range(0, 10, 2)
print(my_range.index(4))  # 2

decimals = range(0, 100)
my_range = decimals[3: 40: 3]

print(my_range)

for i in my_range:
    print(i)  # 3, 6, .. 39

print("=" * 40)
for i in range(3, 40, 30):
    print(i)

print(my_range == range(3, 40, 3))  # True

# also True as they produce the same values
print(range(0, 5, 2) == range(0, 6, 2))

r = range(0, 100)

for i in r[::-2]:
    print(i)  # 99, .., 1

print("=" * 50)

for i in range(99, 0, -2):  # numbers reversed
    print(i)  # same as above

print(range(0, 100)[::-2] == range(99, 0, -2))  # True
for i in range(0, 100, -2):
    print(i)  # empty, tries to count back from 0

backString = "nohytP"
print(backString[::-1])

r = range(10)
for i in r[::-1]:
    print(i)
