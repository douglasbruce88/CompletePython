cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open(".\\Section 10\\cities.txt", 'w') as city_file:
    for city in cities:
        # default is to not flush buffer immediately
        # might want to flush if writing to the screen
        # and you want your user to see it immediately
        print(city, file=city_file)  # cant have spaces around file=

cities = []
with open(".\\Section 10\\cities.txt", 'r') as city_file:
    for city in city_file:
        # strip otherwise each one has \n at the end
        cities.append(city.strip('\n'))

print(cities)

# removed first letter
print("Adelaide".strip('A'))

# will remove the final 'e' as it's at the end of the word
# and a partial match but not the 'el' as it's not at the end,
# even though it's a full match
print("Adelaide".strip('el'))

imelda = (
    "More Mayhem",
    "Imelda May",
    2011,
    ((1, "Pulling The Rug"), (2, "Psycho")))

# will write as a so hard to read back in as a tuple
with open(".\\Section 10\\imelda.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

# ... but can do using eval though it's not ideal
with open(".\\Section 10\\imelda.txt", 'r') as imelda_file:
    imelda = eval(imelda_file.readline())

print(imelda)
title, artist, year, tracks = imelda
print(title)
