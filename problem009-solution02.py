__author__ = 'b543840'
import math
import fractions

s = 1000
s2 = s / 2
mlimit = int(math.floor(math.sqrt(s2) - 1))
for m in range(2, mlimit):
    if s2 % m == 0:
        sm = s2 / m
        while sm % 2 == 0:  # reduce the search space by
            sm /= 2  # removing all factors 2
    if m % 2 == 1:
        k = m + 2
    else:
        k = m + 1
    while k < 2 * m and k <= sm:
        if sm % k == 0 and fractions.gcd(k, m) == 1:
            d = s2 / (k * m)
            n = k - m
            a = d * (m * m - n * n)
            b = 2 * d * m * n
            c = d * (m * m + n * n)
            print (a, b, c)
        k += 2


