import math
import time
timer = time.time
t0 = timer()

limit = 20000000

sievebound = (limit - 1) / 2  # last index of sieve
sieve = [False] * sievebound
crosslimit = int(math.floor(math.sqrt(limit) - 1) / 2)
for i in range (1, crosslimit):
    if not sieve[i]:  # 2*i*j is prime, mark multiples
        for j in range(2 * i * (i + 1), sievebound, 2 * i + 1):
            sieve[j] = True
sum = 2
for i in range(1, sievebound):
    if not sieve[i]:
        sum += 2 * i + 1

print "Sum: " + str(sum)
print "Seconds: " + str(timer() - t0)
