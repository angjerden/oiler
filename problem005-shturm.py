__author__ = 'b543840'

import operator

factors = list()
for f in xrange(2, 20):
    for n in factors:
        if f % n == 0:
            f = f / n
    if f != 1:
        factors.append(f)
num = reduce(operator.mul, factors, 1)

print num
print factors