import shelve

blt = ["bacon", "lettuce" "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open(".\\Section 10\\recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["scrambled_eegs"] = scrambled_eggs
    recipes["pasta"] = pasta

with shelve.open(".\\Section 10\\recipes") as recipes:
    recipes["soup"] = soup  # soup included in printout

    # appends to an in-memory copy but does not update shelf
    recipes["blt"].append("butter")
    for snack in recipes:
        print(snack, recipes[snack])
