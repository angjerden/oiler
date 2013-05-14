__author__ = 'b543840'
import time

default_timer = time.time
t0 = default_timer()

divide_min = 1
divide_max = 20
smallest_not_found = True
smallest_evenly_divisible = 0
current_number = 1

while smallest_not_found:
    found = True
    for j in range(divide_min, divide_max):
        if current_number % j != 0:
            found = False
            break
    if found:
        smallest_evenly_divisible = current_number
        smallest_not_found = False
    current_number += 1

print "The smallest evenly divisible number by numbers " + \
      str(divide_min) + " to " + str(divide_max) + ": " + str(smallest_evenly_divisible)

print default_timer() - t0