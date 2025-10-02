__author__ = "Fabian Ha"

import math
from typing import Tuple


def fermats_factorization_method(n: int, max: int = None) -> Tuple[int, int, int]:
    att = 1
    a = math.isqrt(n)
    while a * a < n:
        a += 1

    b = math.sqrt(a * a - n)

    while not b % 1 == 0:
        a += 1
        if max and att > max:
            raise Exception(f"Fermats factorization method needs more than {max} trys!")
        b = math.sqrt(a * a - n)
        att += 1

    p = a - b
    q = a + b

    return int(p), int(q), att


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Fabians RSA-Attack")
    parser.add_argument("-v", "--verbose", action="store_true", required=False, default=False)
    parser.add_argument("-m", metavar="MAX", required=False, type=int, action="store")
    parser.add_argument("modul", metavar="modul", type=int, action="store")
    args = parser.parse_args()

    p, q, attempts = fermats_factorization_method(args.modul, args.m)
    print(f"Es braucht {attempts} Versuche, um die Faktoren von {args.modul} zu finden:")
    print("p = ", p)
    print("q = ", q)

    # p und q sollten weit genug voneinander entfernt sein, weil man sonst wenige Versuche braucht um auf die zweite Primzahl zu kommen
