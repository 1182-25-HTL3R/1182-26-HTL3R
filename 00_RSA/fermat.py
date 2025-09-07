__author__ = 'Fabian Ha'

import doctest
from collections import Counter


def fermat(n: int) -> Counter:
    """
    calculates the Fermat numbers for a whole number
    :param n: the whole number greater than 1
    :return: a Counter Object of Fermat numbers

    >>> counter = fermat(2); counter.most_common()
    [(1, 1)]
    >>> counter = fermat(9); counter.most_common()
    [(1, 2), (4, 2), (0, 2), (7, 2)]
    >>> counter = fermat(569); counter.most_common()
    [(1, 568)]
    """
    l = []
    if n < 2:
        raise ValueError('n must be greater than 1')
    for i in range(1, n):
        l.append(pow(i, n - 1) % n)

    return Counter(l)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    for p in [2, 3, 5, 7, 11, 997, 9, 15, 21]:
        c = fermat(p)
        print(
            f'{p} -> {int(c.get(1) * 100 / c.total())} % -> res[1]={c.get(1)}, len(res)={len(c.keys())} - {c.most_common()}')

    for p in range(551, 570):
        c = fermat(p)
        print(
            f'{p} -> {int(c.get(1) * 100 / c.total())} % -> res[1]={c.get(1)}, len(res)={len(c.keys())} - {c.most_common()}')

    for p in [6601, 8911]:
        c = fermat(p)
        print(
            f'{p} -> {int(c.get(1) * 100 / c.total())} % -> res[1]={c.get(1)}, len(res)={len(c.keys())} - {c.most_common()}')
