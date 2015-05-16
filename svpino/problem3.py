__author__ = 'anders'

# Problem 3
#
# Write a function that computes the list of the first
# 100 Fibonacci numbers. By definition, the first two
# numbers in the Fibonacci sequence are 0 and 1,
# and each subsequent number is the sum of the
# previous two. As an example, here are the first
# 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def compute(f, nr):
    while len(f) <= nr:
        f.append(f[-2] + f[-1])
    return f

if __name__ == '__main__':
    fibonacci = [0, 1]
    print(str(compute(fibonacci, 100)))