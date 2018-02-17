# Unless you store a time with timezone, you can't tell which local time
# you have when passing through a time change. To fix this, immediately
# convert to UTC and display back to local when displaying

import datetime

import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

# Localises a naive datetime (i.e. one with no timezone information),
# all it does is assume UTC in this case
aware_local_time = pytz.utc.localize(local_time)
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, timezone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC time {}, timezone {}".format(aware_utc_time, aware_utc_time.tzinfo))

aware_time_zone = pytz.utc.localize(utc_time).astimezone()
print("Aware time {}, timezone {}".format(aware_utc_time, aware_utc_time.tzinfo))

# This is ambiguous
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())  # will give different number depending on where it's run

s = 1445733000
t = s + (60 * 60)
gb = pytz.timezone('GB')

# fromtimestamp will return local date, need to use utcfromtimestamp
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

# Both print the same time!
print("{} seconds since epoch is {}".format(s, dt1))
print("{} seconds since epoch is {}".format(t, dt2))
