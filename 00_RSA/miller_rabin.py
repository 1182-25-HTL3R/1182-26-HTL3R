__author__ = 'Fabian Ha'

import random


def is_prime(number):
    if number < 2:
        return False

    first_hundred_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                            37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                            83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
                            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                            197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
                            263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                            331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
                            397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
                            461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
                            541]

    for prime in first_hundred_primes:
        if number % prime == 0 and number / prime == 1:
            return True

    return True if is_prim_millerabin(number, 20) == 'probably prime' else False


def is_prim_millerabin(n, k):
    if n <= 3:
        raise ValueError("n must be greater than 3")

    if k < 1:
        raise ValueError("k must be at least 1")

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d = d // 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        y = pow(a, d, n)

        if y == 1 or y == n - 1:
            continue

        for _ in range(r - 1):
            y = pow(y, 2, n)
            if y == n - 1:
                break
        else:  # different approach than in instructions because named loops don't exist in python
            return "composite"
    return "probably prime"


def generate_prime(bits):
    while True:
        max_n = (1 << bits) - 1
        number = random.SystemRandom().randint(max_n // 2, max_n)
        number |= 1
        if is_prime(number):
            return number


if __name__ == '__main__':
    for i in range(10):
        print(generate_prime(256))
