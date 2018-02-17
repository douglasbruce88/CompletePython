# time, datetime and calendar.
# only need time if dealing with times rather than actual dates
# 32 bit system dates cut off at 2038

import time

print(time.gmtime(0))  # epoch as a struct_time
print(time.localtime())  # now as a struct_time
print(time.localtime(time.time()))
print(time.time())  # seconds since epoch as a float

time_here = time.localtime()
print("Year:", time_here[0], time_here.tm_year)  # repeats year
print("Month:", time_here[1], time_here.tm_mon)  # repeats month
print("Day:", time_here[2], time_here.tm_mday)  # repeats day


from time import time as my_timer # use for dealing with real times
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))

# Issues with this: can press enter twice quickly to cheat, time might not be accurate
# if over the boundary of daylight savings time or if the system clock change
# both of the below work
from time import monotonic as my_timer # not typically used
from time import perf_counter as my_timer # best way
from time import process_time as pt # CPU timer

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))
