__author__ = 'b543840'

#Triangular number formula: Xn = n(n+1)/2
import math
import time
timer = time.time
t0 = timer()

limit_divs = 500
found = False
n = 1

while not found:
    trinum = n * (n + 1) / 2
    divs = 0
    range_limit = 0
    if n < 10:
        range_limit = n
    else:
        range_limit = int(math.floor(math.sqrt(trinum)))
    for j in range(1, range_limit):
        if trinum % j == 0:
            divs += 2
    print str(trinum) + " : " + str(divs)
    if divs > limit_divs:
        print "WE HAVE A WINNER!!!!!!!!!!!!!!!!!!!!!"
        print str(trinum) + " : " + str(divs)
        div = list()
        for j in range(1, trinum):
            if trinum % j == 0:
                div.append(j)
        print "Divisors: " + str(div)
        found = True

    n += 1

print "Seconds: " + str(timer() - t0)