__author__ = 'b543840'
import time

timer = time.time
t = timer()

limit = 1001

for a in range(1, limit):
    for b in range(a + 1, limit):
        for c in range(b + 1, limit):
            sqa = a ** 2
            sqb = b ** 2
            sqc = c ** 2
            if (sqa + sqb) == sqc and (a + b + c) == 1000:
                print str(a) + "^2 + " + str(b) + "^2 = " + str(sqa + sqb)
                print str(c) + "^2 = " + str(sqc)
                print "a + b + c = " + str(a + b + c)
                print "a * b * c = " + str(a * b * c) + "\n"

    print "a: " + str(a)
print "Seconds: " + str(timer() - t)