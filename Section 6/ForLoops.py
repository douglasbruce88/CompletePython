for i in range(1, 20):
    print(i)  # prints 1..19

number = "9,223,372,036,854,775,807"
cleanedNumber = ""
for i in range(0, len(number)):
    # print(number[i])
    if number[i] in '0123456789':
        print(number[i], end='')
        cleanedNumber += number[i]

print("")
print("The number is {0}".format(int(cleanedNumber)))

for char in number:
    if char in '0123456789':
        print(char, end='')

print("")
for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

for i in range(0, 100, 5):
    print(i)  # 0, 5, ..., 95

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i * j))
    print("================")
