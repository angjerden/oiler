__author__ = 'b543840'

highest_start = 0
highest = 0
for i in range(999999, 4000, -1):
    num = i
    terms = 1
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        terms += 1
    if terms > highest:
        highest_start = i
        highest = terms
        print "================ NEW HIGHEST =========== >>>"
    print "Number of terms for starting number " + str(i) + " : " + str(terms)

print "Highest was " + str(highest_start) + " with " + str(highest) + " terms"