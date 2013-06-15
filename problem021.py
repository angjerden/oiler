__author__ = 'anders'

import time
timer = time.time
start_time = timer()

sums = dict()

def sumpropdiv(n):
    if n in sums:
        #print "Found sum of " + str(n) + " in sums: " + str(sums[n])
        return sums[n]
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
            # print str(i) + " is a proper divisor of " + str(n)
    sums[n] = sum
    return sum

if __name__ == "__main__":
    amicable = dict()
    for i in range(1, 10000):
        sum = sumpropdiv(i)
        sum_2 = sumpropdiv(sum)
        if i == sum_2 and i != sum:
            print "####### Amicable numbers: " + str(i) + " + " + str(sum)
            if i not in amicable:
                amicable[i] = 1
            if sum not in amicable:
                amicable[sum] = 1

    amicable_sum = 0
    for key in amicable.keys():
        amicable_sum += key
    print amicable_sum

print "Seconds elapsed: " + str(timer() - start_time)