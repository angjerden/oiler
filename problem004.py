__author__ = 'b543840'

highest = 0
rangemin = 100
rangemax = 1000

if __name__=="__main__":
    for i in range(rangemin, rangemax):
        for j in range(i, rangemax):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > highest:
                    highest = product
                    print "Current highest palindromic product: " +\
                          str(i) + " * " + str(j) + " = " + str(highest)