# Write al program to display info on the four clock's we've just seen

import time

clocks = ['time', 'monotonic', 'process_time', 'perf_counter']

for clock in clocks:
    info = time.get_clock_info(clock)
    print(clock, info)
