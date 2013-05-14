__author__ = 'b543840'
import math
import time
default_timer = time.time
t0 = default_timer()

primes = [2]
max = 10001

i = 2
while len(primes) < max + 1:
    number = i
    square = math.sqrt(number)
    dont_add = False
    for prime in range(primes[0], primes[len(primes) - 1]):
        if prime > square or dont_add is True:
            break
        if number % prime == 0:
            dont_add = True
    if dont_add is False and number not in primes and number != 1:
        primes.append(number)
    i += 1

print str(primes)
print str(primes[5])
print str(primes[999])
print str(primes[10000])

print "Seconds: " + str(default_timer() - t0)