# take text and return a list of all consonants,
# sorted in alphabetical order

input_str = "this is some text"

vowels = frozenset(" aeiou")
answer = set(input_str).difference(vowels)

print(sorted(answer))
