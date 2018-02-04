ipAddress = "192.168.0.1"

print(ipAddress.count("."))

parrot_list = ["not pinin'", "no more", "a stiff", "bereft of life"]

parrot_list.append("a Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd  # concats
numbers.sort()  # in place, doesnt return modified list, returns None
sortedNums = sorted(numbers)  # returns a new list
print(numbers)

if numbers == sortedNums:
    print("equal")  # hit if numbers are sorted (SequenceEqual)
else:
    print("not equal")  # hit if numbers are unsorted

# both empty lists, are  equal
list_1 = []
list_2 = list()

if list_1 == list_2:
    print("lists equals")

print(list("the lists are equal"))  # list of chars

even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
print(even)  # prints 8, 6, 4, 2

print(another_even is even)  # true
print(even is list(even))  # false, checks for memory loc
print(even == another_even)  # true

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)  # list of the two lists

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
