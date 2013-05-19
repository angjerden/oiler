__author__ = 'b543840'

big = str(2 ** 1000)
print len(big)
print big

sum = 0
for i in range(0, len(big)):
    sum += int(big[i:i+1])

print sum