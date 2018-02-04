greeting = "Bruce"
_myName = "Doug"
Doug45 = "Good"
Doug_Was_57 = "Hello"
Greeting = "There"

age = 24
print(age)

# Type error
# print(greeting + age)

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # returns float
print(a // b)  # returns int
print(a % b)

for i in range(1, a // b):
    print(i)  # prints 1, 2, 3

parrot = "Norwegian Blue"
print(parrot[3])  # w, 0 based
print(parrot[-1])  # e
print(parrot[0:6])  # Norweg
print(parrot[:6])  # Norweg
print(parrot[6:])  # ian Blue
print(parrot[-4:-2])  # Bl
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])  # just commas
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])  # just the numbers

print("Hello " * 5)

today = "friday"
print("day" in today)
print("thur" in today)
