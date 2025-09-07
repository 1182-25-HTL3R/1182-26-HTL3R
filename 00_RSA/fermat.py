__author__ = 'Fabian Ha'

def fermat(n: int) -> list:
    """
    calculates the Fermat numbers for a whole number
    :param n: the whole number greater than 1
    :return: a list of Fermat numbers
    """
    l = []
    if n < 2:
        raise ValueError('n must be greater than 1')
    for i in range(1, n):
        value = pow(i, n-1) % n
        l.append(value)

    return l

for p in [2, 3, 5, 7, 11]:
    print(fermat(p))

print(fermat(997))
