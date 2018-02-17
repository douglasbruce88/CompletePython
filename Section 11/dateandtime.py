# Use the datetime module, better than the time module
# even though time includes dates

# time.timezone and time.tzname:
# number of seconds offset from UTC and name  both DST and no DST time zone

import time

# look up strftime for all the %x options (lots!) %Z deprecated.
print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Daylight Saving Time")
else:
    print("Not DST")

print("Local time is " + time.strftime('%y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%y-%m-%d %H:%M:%S', time.gmtime()))

# there are 'aware' and 'naive' objects in here which are/not aware of timezone offsets
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
