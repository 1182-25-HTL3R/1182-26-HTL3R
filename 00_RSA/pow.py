__author__ = "Fabian Ha"

import doctest
import time


def my_pow(x: int, b: int, n: int = None) -> int:
    """
    Implementation of the fast exponential function pow()
    :param x: Base
    :param b: Exponent
    :param n: Modulus
    :return: Result of fast exponential function

    >>> my_pow(5, 4)
    625
    >>> my_pow(5, 4, 2)
    1
    >>> my_pow(2, 777, 8)
    0
    """
    if b < 0: raise ValueError("b must be greater or equal to 0")

    erg = 1
    while b > 0:
        if b & 1 == 1:
            erg = erg * x if n is None else (erg * x) % n
        x = x * x if n is None else (x * x) % n
        b = b >> 1

    return erg


if __name__ == "__main__":
    doctest.testmod()
    # A.2 Aufgabe - Vergleichen:
    print(my_pow(84, 18, 45) == pow(84, 18, 45))
    print(my_pow(4, 209, 59) == pow(4, 209, 59))

    print()

    # A.2 Aufgabe - Rechenzeit:
    print("--- normal ---")
    start_time = time.time_ns()
    print((2 ** 123456789) % 9)
    print(f"took: {(time.time_ns() - start_time) / 1000} ms")

    print()

    print("--- my pow ---")
    start_time = time.time_ns()
    print(my_pow(2, 123456789, 9))
    print(f"took: {(time.time_ns() - start_time) / 1000} ms")

    print()

    print("--- pow ---")
    start_time = time.time_ns()
    print(pow(2, 123456789, 9))
    print(f"took: {(time.time_ns() - start_time) / 1000} ms")
