__author__ = 'b543840'


target = 600851475143
i = 2

print "Finding prime factors of " + str(target)
while target >= i:
    if target % i == 0:
        print str(i)
        target = target / i
    i += 1
