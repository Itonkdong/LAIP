import math


def is_prime(x):
    if x == 1 or x == 2:
        return False

    for i in range(2, math.floor(x ** (0.5)) + 1, 1):
        if x % i == 0:
            return False

    return True


if __name__ == '__main__':
    odd_numbers = [x for x in range(1, 30, 2)]
    primes = [x for x in range(1, 100) if is_prime(x)]
    matrix = [[i * j for j in range(1,5)] for i in range(1,4)]
    print(odd_numbers)
    print(primes)
    print(matrix)
