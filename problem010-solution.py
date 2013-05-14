import math
import time
timer = time.time
t0 = timer()
limit = 2000000
crosslimit = int(math.floor(math.sqrt(limit)))
sieve = [False] * limit
for n in range(4, limit, 2):
    # mark even numbers > 2
    sieve[n] = True

for n in range(3, crosslimit + 1, 2):
    if not sieve[n]:
        # n not marked, hence prime
        for m in range(n*n, limit, 2*n):
            sieve[m] = True

sum = 0
for n in range(2, limit):
    if not sieve[n]:
        sum += n
        #print n

print "Sum: " + str(sum)
print "Seconds: " + str(timer() - t0)