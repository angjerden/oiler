__author__ = 'b543840'

min = 1
max = 100
sum_of_squares = 0
sum = 0
for i in range(min, max + 1):
    sum_of_squares += i ** 2
    sum += i

square_of_the_sum = sum ** 2
diff = square_of_the_sum - sum_of_squares
print "The difference is : " + str(diff)