__author__ = 'anders'

# Problem 2
#
# Write a function that combines two lists by alternatingly
# taking elements. For example: given the two lists
# [a, b, c] and [1, 2, 3], the function should
# return [a, 1, b, 2, c, 3].

def combine(a, b):
    max = len(a) if len(a) > len(b) else len(b)
    arr = []
    for i in range(0, max):
        if(i <= len(a)):
            arr.append(a[i])
        if(i <= len(b)):
            arr.append(b[i])
    return arr

if __name__ == '__main__':
    a = ['a', 'b', 'c']
    b = [1, 2, 3]

    print(str(combine(a,b)))