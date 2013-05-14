__author__ = 'b543840'

accumulated = 0
rangemax = 1000

for i in range(1, rangemax):
    if i % 3 == 0:
        accumulated += i
    elif i % 5 == 0:
        accumulated += i

print accumulated
