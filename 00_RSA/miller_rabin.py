__author__ = 'Fabian Ha'

import random

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

        if y == 1 or y == n-1:
            continue

        for _ in range(r - 1):
            y = pow(y, 2, n)
            if y == n - 1:
                break
        else:               # different approach than in instructions because named loops don't exist in python
            return "composite"
    return "probably prime"

if __name__ == '__main__':
    for i in range(4, 1000):
        s = is_prim_millerabin(i, 20)
        if s == "probably prime":
            print(i)