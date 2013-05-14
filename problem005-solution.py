__author__ = 'b543840'
import math
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

k = 20
N = 1
i = 1
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check = True
limit = math.sqrt(k)
while p[i] <= k:
    a[i] = 1
    if check:
        if p[i] <= limit:
            a[i] = math.floor(math.log(k) / math.log(p[i]))
        else:
            check = False
    N *= p[i] ** a[i]
    i += i
print N