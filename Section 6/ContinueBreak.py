shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        continue  # just misses spam
    print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break  # misses all after spam
    print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        nasty_food_item = item
        break
else:  # runs if the loop reaches completion
    nasty_food_item = ""
    print("I'll have a plate of that")

if nasty_food_item:
    print("Can't I have anything without spam in it")
