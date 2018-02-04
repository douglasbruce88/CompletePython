string = "1234567890"

# implicit iter creation
for char in string:
    print(char)

# same as first loop but explicit
for char in iter(string):
    print(char)

# manual for loop
my_iterator = iter(string)

print(my_iterator)  # obj reference

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))  # error, StopIteration
