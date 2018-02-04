# double slash to avoid warning and special chars
# VSCode runs in 'folder' dir, not subfolder
path = ".\\Section 10\\sample.txt"

# r is the default
sample = open(path, 'r')
for line in sample:
    print(line, end='')  # prints two line spaces without end = ''
sample.close()

print()
print('-' * 40)

# this is more pythonic. with handles errors
# and ensures that the file is closed before termination
with open(path) as sample:
    for line in sample:
        if "2" in line:
            print(line, end='')

print('-' * 40)

with open(path) as sample:
    line = sample.readline()  # reads a single line into a string
    while line:
        print(line, end='')
        line = sample.readline()

print()
print('-' * 40)
with open(path) as sample:
    lines = sample.readlines()  # returns a list of strings, could cause memory problems
    # prints ['Line 1\n', 'Line 2\n', '\n', 'Line 3\n', 'Line 4']
    print(lines)
    for line in lines[:: -1]:  # prints lines but in reverse order
        print(line, end='')

with open(path) as sample:
    # reads whole file and if text, returns string list. can also specify how many chars to read
    lines = sample.read()
    for line in lines[:: -1]:  # prints all text reversed
        print(line, end='')
