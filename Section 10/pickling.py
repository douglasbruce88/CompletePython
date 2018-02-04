import pickle

imelda = (
    "More Mayhem",
    "Imelda May",
    2011,
    ((1, "Pulling the Rug"), (2, "Psycho")))

with open(".\\Section 10\\imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

with open(".\\Section 10\\imelda.pickle", "rb") as pickle_file:
    imelda = pickle.load(pickle_file)

print(imelda)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

# can pickle multiple objects
with open(".\\Section 10\\imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(2998302, pickle_file)

# read back in same order as we wrote them
with open(".\\Section 10\\imelda.pickle", "rb") as pickle_file:
    imelda = pickle.load(pickle_file)
    even = pickle.load(pickle_file)
    odd = pickle.load(pickle_file)

print(even)
print(odd)

with open(".\\Section 10\\imelda.pickle", "wb") as pickle_file:
    # produces a more human readable file (but not plan text!)
    # default python3 protocol is number 3, but can't read files
    # using python2 that are created with this protocol
    # protocols 0 and 1 had security checks which had bugs
    # and were removed in protocol 2. instead, don't
    # unpickle data that you don't trust!
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(imelda, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

# security flaw, i can't quite get it to work with the rel path though
pickle.loads(b"cos\nsystem\n(S'del .\\Section 10\\imelda.pickle'\ntR.")
