# dir contains names in current scope
print(dir())  # lots of modules with __ i.e. private and not to be used
for m in dir(__builtins__):
    print(m)  # things such as errors,  None, False/True, print, list

import shelve

print(dir(shelve))  # includes open but not close

# includes close as it's a method of the Shelf class
# can navigate to the source of shelve of Shelf in the IDE
for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

# useful to look at these things to get an idea of how you should
# document your own libraries
help(shelve.Shelf)  # lots of documentation! uses webbrowser
