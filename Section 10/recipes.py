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

    # this works though
    tmp = recipes["blt"]
    tmp.append("butter")
    recipes["blt"] = tmp
    for snack in recipes:
        print(snack, recipes[snack])

# other way to append to items. this doesn't write to
# the shelf until you close the shelf or call sync.
# writeback caches the shelf in memory so is more intensive
with shelve.open(".\\Section 10\\recipes", writeback=True) as recipes:
    recipes["soup"].append("croutons")
    recipes.sync()
    recipes["soup"].append("cream")

    for snack in recipes:
        # this will include cream as it's in the cached version
        print(snack, recipes[snack])

# shelf is a bit like a persistent dictionary or database
# the values can be arbitrarily complex/
# can act like a DB without having to use/learn SQL
# values pickled & unpickled for saving so if they are too complex,
# this may take some time and not be platform agnostic.
# also problems with security and the shelf items being corrupted online
# concurrency not great either
