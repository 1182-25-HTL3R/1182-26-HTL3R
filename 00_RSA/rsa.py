import math
import random

from miller_rabin import generate_prime


def generate_keys(number_of_bits):
    p = generate_prime(number_of_bits // 2)
    q = generate_prime(number_of_bits // 2)

    n = p * q
    while n.bit_length() > number_of_bits:
        n = p * q

    phi = (p - 1) * (q - 1)

    e = random.SystemRandom().getrandbits(256)
    while math.gcd(e, phi) != 1:
        e = random.SystemRandom().getrandbits(256)

    d = pow(e, -1, (p - 1) * (q - 1))

    return (e, n, e.bit_length()), (d, n, d.bit_length())


def file2ints(file_path, bytenumber):
    with open(file_path, "rb") as file:
        while block := file.read(bytenumber):  # walrus operator is cool
            yield int.from_bytes(block)


if __name__ == "__main__":
    public_key, private_key = generate_keys(128)
    for x in [1, 15, 289, 1044]:
        c = pow(x, public_key[0], public_key[1])
        y = pow(c, private_key[0], private_key[1])
    assert x == y

    ints = file2ints("message.txt", 8)
    for i in ints: print(i)
