# allows you to launch a web browser and navigate to a URL
import webbrowser

# will try to open new window if possible but doesn't work in Chrome
webbrowser.open("https://www.python.org/", new=1)
webbrowser.open_new("https://www.python.org/")  # just calls open with new=1

help(webbrowser)

for i in range(10):
    # hover over gives 'values, ...' which means
    # we can call print with many values
    print(i)
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep="; ")  # sep is a 'named argument'


# use a browser other than the system default
ie = webbrowser.get(using=webbrowser.iexplore)
ie.open("https://www.bbc.co.uk")

# webbrowser.register() used to register new browsers e.g. Edge
