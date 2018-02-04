for i in range(10):
    print(i)

# same as above
i = 0
while i < 10:
    print(i)
    i += 1

available_exits = ["east", "north east", "south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = "east"  # choose a direction, could be from input
    # point is that you don't know in advance when to exit
    # e.g. reading from file
    if chosen_exit == "quit":
        print("Game over")
        break
else:
    print("Got out")

import random
answer = random.randint(1, 10)

guess = 0
while guess != answer:
    if guess < answer:
        print("Guess higher")
        guess = answer
    else:
        print("Guess lower")
else:
    print("Well done")
