import time

timer = time.time
t = timer()

s = 1000

for a in range(3, (s - 3) / 3):
    for b in range(a + 1, (s - 1 - a) / 2):
        c = s - a - b
        sqa = a ** 2
        sqb = b ** 2
        sqc = c ** 2
        if (sqa + sqb) == sqc:
            print str(a) + "^2 + " + str(b) + "^2 = " + str(sqa + sqb)
            print str(c) + "^2 = " + str(sqc)
            print "a + b + c = " + str(a + b + c)
            print "a * b * c = " + str(a * b * c) + "\n"

print "Seconds: " + str(timer() - t)