# hex useful as shorter than binary but conversion is easy
# 4 digits can represent up to 65536 items

for i in range(17):
    print("{0:>2} in hex is {0:0>2x}".format(i))

# use 0x prefix to identify hex
x = 0x20
print(x)  # 32, not 20
print(x * x)  # 1024

# octal used for (e.g.) linux file permissions
