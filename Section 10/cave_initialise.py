# write these to two shelves
import shelve


vocabulary = {
    "QUIT": "Q",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3"}

with shelve.open(".\\Section 10\\locations") as locations:
    locations["0"] = {"desc": "computer",
                      "exits": {},
                      "namedExits":  {}}
    locations["1"] = {"desc": "road",
                      "exits": {"W": 2, "E": 3},
                      "namedExits": {"2": 2, "3": 3}}
    locations["2"] = {"desc": "hill",
                      "exits": {"N": 5, "Q": 0},
                      "namedExits": {"5": 5}}

with shelve.open(".\\Section 10\\vocabulary") as vocabulary:
    vocabulary["QUIT"] = "Q"
    vocabulary["ROAD"] = "1"
    vocabulary["HILL"] = "2"
    vocabulary["BUILDING"] = "3"
