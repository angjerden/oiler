__author__ = 'b543840'
import time
from time import sleep

default_timer = time.time
t0 = default_timer()

s = """20 30 40 50
49 59 69 79"""


arr = s.split("\n")
arr1 = []
line_counter = 0
el_counter = 0
for line in range(0, len(arr)):
    arr1.insert(line_counter, arr[line_counter].split(" "))
    line_counter += 1
print arr1


print default_timer() - t0


