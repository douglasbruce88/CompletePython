l = [1, 2, 3, 4, 5]
i = iter(l)

for j in range(0, len(l)):  # no len on iterator
    print(next(i))

# shorthand version
for j in l:
    print(l)
