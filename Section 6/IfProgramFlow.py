name = "Doug"
age = 29

if age >= 18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years".format(18 - age))

guess = 4

if guess < 5:
    print("Please guess higher")
    guess += 1
    if guess == 5:
        print("Well done")
    else:
        print("Sorry")
elif guess != 5:
    print("Please guess lower")
    guess -= 1
    if guess == 5:
        print("Well done")
    else:
        print("Sorry")
else:
    print("Got it first time")

if (age >= 16) and (age <= 65):  # shortcut eval
    print("Have a good day at work")

if 16 <= age <= 65:
    print("Ditto")

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Enjoy your day at work")

x = "false"

if x:
    print("x is true")  # nonzeros evaluate to true

# all the below are false
print("""False:{0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(
    False,
    bool(None),
    bool(0),
    bool(0.0),
    bool([]),
    bool(()),
    bool(''),
    bool(""),
    bool({})))

x = ''

if x:
    print("You entered {0}".format(x))

print(not False)
print(not True)

if not age < 18:
    print("You can vote")

parrot = "Norwegian Blue"

letter = "b"

if letter in parrot:  # False (in is case sensitive)
    print("Good guess")
else:
    print("Not in the word")
