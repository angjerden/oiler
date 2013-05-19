__author__ = 'b543840'
import time
from time import sleep

default_timer = time.time
t0 = default_timer()

arr = [[]]
arr[0].append('aa1')
arr[0].append('aa2')
arr.append([])
arr[1].append('bb1')


print default_timer() - t0


