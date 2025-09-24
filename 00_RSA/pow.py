import doctest


def my_pow(x: int, b: int, n: int = None) -> int:
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
    print(my_pow(5, 4))
    print(my_pow(5, 0))
    print(my_pow(5, -1))
