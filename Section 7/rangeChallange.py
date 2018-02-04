start = 0
stop = 10  # default None
step = 2  # default 1
r = range(start, stop, step)

r2 = range(100)[start:stop:step]

print(r)
print(r2)

print(r == r2)  # true

print(range(100)[:10:2] == r)  # True
