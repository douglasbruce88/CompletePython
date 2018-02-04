# Dictionaries as shelve entries
import shelve

books = shelve.open(".\\Section 10\\book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["blt"])
print(books["maintenance"]["loose"])
