__author__ = 'Fabian Ha'

from collections import Counter


def fermat(n: int) -> Counter:
    """
    calculates the Fermat numbers for a whole number
    :param n: the whole number greater than 1
    :return: a Counter Object of Fermat numbers
    """
    l = []
    if n < 2:
        raise ValueError('n must be greater than 1')
    for i in range(1, n):
        l.append(pow(i, n - 1) % n)

    return Counter(l)


for p in [2, 3, 5, 7, 11, 997, 9, 15, 21]:
    c = fermat(p)
    print(
        f'{p} -> {c.get(1) * 100 / c.total():.0f} % -> res[1]={c.get(1)}, len(res)={len(c.keys())} - {list(c.items())}')

for p in range(551, 570):
    c = fermat(p)
    print(
        f'{p} -> {c.get(1) * 100 / c.total():.0f} % -> res[1]={c.get(1)}, len(res)={len(c.keys())} - {list(c.items())}')

for p in [6601, 8911]:
    c = fermat(p)
    print(
        f'{p} -> {c.get(1) * 100 / c.total():.0f} % -> res[1]={c.get(1)}, len(res)={len(c.keys())} - {list(c.items())}')
