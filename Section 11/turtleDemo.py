done = "Well done"

import turtle
# can just import certain parts of a module and then don't prefix
# useful if using the functions a lot but we need to keep adding
# to the list if we want another function from the module
# importing both as in this example isn't ideal as it's confusing
from turtle import forward

# this is also not advised and we get unused import warnings
# we don't know what's being imported and can hide our own methods
from turtle import *

# warnings below are a bug
forward(150)
turtle.right(250)
forward(150)
done()
print(done)  # this doesn't do what's expected due to the import *
