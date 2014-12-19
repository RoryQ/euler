import math

def decimal_to_factoradic(num):
    # compute largest divisible factorial
    n = 0
    while(math.factorial(n + 1) < num): n += 1

    # divide by decreasing factorials
    divs = []
    while(n >= 0):
        (div, num) = divmod(num, math.factorial(n))
        divs.append((div, num, n))
        n -= 1
    return int(''.join([str(a[0]) for a in divs]))

def factoradic_to_permutation(fact, base=10):
    indexes = [int(x) for x in str(fact)]
    l = [x for x in range(base)]
    return ''.join([str(l.pop(x)) for x in indexes])

if __name__ == '__main__':
    # permutation 0 is 0123456789 so minus 1
    fact = decimal_to_factoradic(1000000-1)
    print factoradic_to_permutation(fact)
