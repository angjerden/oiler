__author__ = 'b543840'

fibdict = {1:1, 2:2}
target = 48
upper_limit = 4000000
even_valued_sum = 0

def fib(n):
    if n in fibdict:
        return fibdict[n]
    else:
        fibdict[n] = fib(int(n)-2) + fib(int(n)-1)
        return fibdict[n]

if  __name__ =='__main__':
    fib(target)
    output = "The " + str(target) + "'th Fibonacci number is: \n"
    for i in fibdict.keys():
        if i < target:
            output+= str(fibdict[i]) + " + "
        if i % 10 == 0:
            output += "\n"
        if fibdict[i] < upper_limit and fibdict[i] % 2 == 0:
            even_valued_sum += fibdict[i]
    print output + " = " + str(fibdict[target])

    print "The sum of even-valued Fibonacci numbers " \
             "not exceeding " + str(upper_limit) + ": " + str(even_valued_sum)
