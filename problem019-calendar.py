__author__ = 'b543840'

import time
from datetime import date
start = date(1900, 01, 01)
print start.weekday()

num_of_sundays = 0

for i in range(1901, 2001):
    for j in range(1, 13):
        current_date = date(i, j, 01)
        if current_date.weekday() == 6:
            num_of_sundays += 1
            print str(current_date) + " was a sunday"

print "Number of sundays on the first day of the month: " + str(num_of_sundays)