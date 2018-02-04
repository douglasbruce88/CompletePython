# convert an int (< 65536) to binary without using a format string

in1 = 53513
in2 = 39

target = in2
answer = []
for i in range(15, -1, -1):
    topVal = 2 ** i
    if target >= topVal:
        answer.append("1")
        target -= topVal
    else:
        if answer:  # avoid print leading zeros
            answer.append("0")

print("".join(answer))

# then do octal
target = in2
octAnswer = []
for i in range(4, -1, -1):
    topVal = 8 ** i
    if target >= topVal:
        mult = target // topVal
        octAnswer.append(str(mult))
        target -= mult * topVal
    else:
        if octAnswer:  # avoid print leading zeros
            octAnswer.append("0")

print("".join(octAnswer))
