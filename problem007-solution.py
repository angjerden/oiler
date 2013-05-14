__author__ = 'b543840'
import math
import time
default_timer = time.time
t0 = default_timer()

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True # we have already excluded 4,6 and 8.
    elif n % 3 == 0:
        return False
    else:
        r=math.floor(math.sqrt(n))  # n rounded to the greatest integer r so that r*r<=n
        f=5
        while f<=r:
            if n % f == 0:
                return False  # (and step out of the function)
            if n %(f+2) == 0:
                return False  # (and step out of the function)
            f += 6
    return True  # (in all other cases)


if __name__ == "__main__":
    limit = 10001
    count = 1  # we know that 2 is prime
    candidate = 1
    while count < limit:
        candidate += 2
        if isPrime(candidate):
            count += 1
    print candidate

print "Seconds: " + str(default_timer() - t0)
