# append times tables to existing file, first col right justified

with open(".\\Section 10\\challenge.txt", 'w') as existing:
    print("Existing", file=existing)

with open(".\\Section 10\\challenge.txt", 'a') as append:
    for i in range(1, 13):
        # what does > do exactly? doesnt seem nevessary
        print("{0:>2} times 2 is {1}".format(i, 2 * i), file=append)
