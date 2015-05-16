__author__ = 'anders'

# Problem 1
#
# Write three functions that compute the sum of the numbers
# in a given list using a for-loop, a while-loop, and recursion.

def sum_for(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum

def sum_while(list):
    sum = 0
    i = 0
    while i < len(list):
        sum += list[i]
        i += 1
    return sum

def sum_rec(list):
    i = 0

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5] #Sum should be 15

    print(str(sum_for(list)))
    print(str(sum_while(list)))