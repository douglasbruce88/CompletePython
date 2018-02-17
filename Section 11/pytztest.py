import datetime

import pytz

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    # Different keys between this and pytz.country_timezones
    # Also multiple timezones for some countries, none for others
    print(x, pytz.country_names[x], end=':')
    if x in pytz.country_timezones:
        print(pytz.country_timezones[x])
    else:
        print("No time zone defined")
