__author__ = 'anders'

divmap = []
divmap.append([])
divmap[0].append(2)
print divmap

for i in range(2, 29):
    sum = 0
    sumstr = str(i) + ": "
    for j in range(1, i):
        if i % j == 0:
            sumstr = sumstr + str(j) + " + "
            sum = sum + j
    if "+" in sumstr:
        sumstr = sumstr[:-3]
    print sumstr + " = " + str(sum)