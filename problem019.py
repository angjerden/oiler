__author__ = 'b543840'

months = dict()
months[1] = 31
months[2] = 28
months[3] = 31
months[4] = 30
months[5] = 31
months[6] = 30
months[7] = 31
months[8] = 31
months[9] = 30
months[10] = 31
months[11] = 30
months[12] = 31

sunday = 7
num_of_sundays = 0

for y in range(1900, 2001):
    for m in range(1, 13):
        if sunday == 1 and y != 1900:
            num_of_sundays += 1
            print str(y) + "." + str(m) + "." + str(sunday) + " was a sunday"
        days_max = months[m]
        if m == 1 and y % 4 == 0 and y % 100 != 0 and y % 400 == 0:   # adding for leap year
            days_max += 1
        while sunday <= days_max:
            sunday += 7
        sunday %= days_max

print "Number of sundays which were first of the month: " + str(num_of_sundays)




