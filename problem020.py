__author__ = 'b543840'

def factorial(n):
    product = 1
    for i in range(n, 0, -1):
        product *= i
    return product

if __name__ == "__main__":
    product = str(factorial(100))
    sum = 0
    for i in range(0, len(product)):
        sum += int(product[i])

print sum

