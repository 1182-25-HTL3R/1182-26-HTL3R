__author__ = 'Fabian Ha'

import doctest
import random


def is_prime(number: int) -> bool:
    """
    Checks if a number is prime
    :param number: Integer number
    :return: True if prime, False otherwise

    >>> is_prime(1)
    False
    >>> is_prime(461)
    True
    >>> is_prime(64433)
    True
    >>> is_prime(64435)
    False
    """
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


def is_prim_millerabin(n: int, k: int) -> str:
    """
    Checks if a number is probably prime with the miller rabin algo
    :param n: Integer number
    :param k: Integer amount of rounds
    :return: 'probably prime' if probably prime, 'composite' otherwise

    >>> is_prim_millerabin(99991, 20)
    'probably prime'
    >>> is_prim_millerabin(84203958029485945, 20)
    'composite'
    >>> is_prim_millerabin(87959, 20)
    'probably prime'
    """
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


def generate_prime(bits: int) -> int:
    """
    Generates a prime number
    :param bits: Maximum bits to generate a number
    :return: Generated prime number
    """
    while True:
        max_n = (1 << bits) - 1
        number = random.SystemRandom().randint(max_n // 2, max_n)
        number |= 1
        if is_prime(number):
            return number


if __name__ == '__main__':
    doctest.testmod(verbose=True)

    # Test für generate_prime(bits)
    for i in range(10):
        print(generate_prime(256))

    # Aufgabe/Test - bestimme die erste Primzahl > 2^512
    # Lösung: 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
    n = (1 << 512) + 1
    while True:
        if is_prime(n):
            print(f'\nNächste Primzahl > 2^512: {n}')
            break
        n += 2

    print()

    # Magic: Ist 24566544301293569 prim?
    # Lösung: True
    magic_number = 24566544301293569
    print(f'Ist 24566544301293569 prim?: {is_prime(magic_number)}\n')

    # Botschaft?
    # Lösung: HTL als 1sen
    # 101011101000
    # 111001001000
    # 101001001110
    # 000000000000
    # 0000001
    print('Magische Botschaft:')
    binary = bin(magic_number)
    binary = binary[2:]
    for i in range(len(binary) // 12):
        print(binary[i * 12:(i + 1) * 12])
    print(binary[(len(binary) // 12) * 12:])
    print()

    # Nächst höhere Zahl immer noch diese Botschaft?
    # Lösung: Ja
    # 101011101000
    # 111001001000
    # 101001001110
    # 000000000000
    # 0010011
    n = magic_number + 2
    while True:
        if is_prime(n):
            print('Magische Botschaft 2:')
            binary = bin(n)
            binary = binary[2:]
            for i in range(len(binary) // 12):
                print(binary[i * 12:(i + 1) * 12])
            print(binary[(len(binary) // 12) * 12:])
            break
        n += 2
