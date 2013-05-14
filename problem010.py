__author__ = 'b543840'
import math
import time
timer = time.time
t0 = timer()

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:  # because all primes above 3 can be written like 6k+1 or 6k-1
                return False
            f += 6
    return True

if __name__ == "__main__":
    limit = 2000000
    sum = 0
    candidate = 2
    while candidate < limit:
        if isPrime(candidate):
            sum += candidate
            print candidate
        if candidate > 2:
            candidate += 2
        else:
            candidate += 1
    print "Sum : " + str(sum)

print "Seconds: " + str(timer() - t0)