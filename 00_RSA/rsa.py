import math
import random
import logging
from typing import Tuple, Generator

from miller_rabin import generate_prime

logger = logging.getLogger("mylogger")


def generate_keys(number_of_bits: int) -> Tuple[Tuple[int, int, int], Tuple[int, int, int]]:
    """
    Generates public and private keys
    :param number_of_bits: blocksize in bits
    :return: public and private keys
    """
    p = generate_prime(number_of_bits // 2)
    q = generate_prime(number_of_bits // 2)
    n = p * q

    while n.bit_length() > number_of_bits or p == q:  # Schlüsselänge muss länger sein als Blocklänge und private und public key unterschiedlich
        p = generate_prime(number_of_bits // 2)
        q = generate_prime(number_of_bits // 2)
        n = p * q

    phi = (p - 1) * (q - 1)

    e = random.SystemRandom().getrandbits(256)
    while math.gcd(e, phi) != 1:
        e = random.SystemRandom().getrandbits(256)

    d = pow(e, -1, phi)

    return (e, n, number_of_bits), (d, n, number_of_bits)


def file2ints(file_path: str, bytenumber: int) -> Generator[int]:
    """
    converts a file into a list of byteblocks as integers
    :param file_path: path to file
    :param bytenumber: number of bytes to read at once
    :return: generator of byteblocks as integers from message
    """
    with open(file_path, "rb") as file:
        while block := file.read(bytenumber):  # walrus operator is cool
            yield int.from_bytes(block)


def save_keys(keys: Tuple[Tuple[int, int, int], Tuple[int, int, int]]) -> None:
    """
    saves the generated keys in files "public_key.txt" and "private_key.txt"
    :param keys: Tuple of public and private keys
    :return: None
    """
    with open("public_key.txt", "w") as f:
        f.write(str(keys[0][0]))
        f.write("\n")
        f.write(str(keys[0][1]))

    logger.info("Public key saved to public_key.txt")

    with open(f"private_key.txt", "w") as f:
        f.write(str(keys[1][0]))
        f.write("\n")
        f.write(str(keys[1][1]))

    logger.info("Private key saved to private_key.txt")


def encrypt_file(file_path: str) -> None:
    return


def decrypt_file(file_path: str) -> None:
    return


if __name__ == "__main__":
    # public_key, private_key = generate_keys(128)
    # for x in [1, 15, 289, 1044]:
    #     c = pow(x, public_key[0], public_key[1])
    #     y = pow(c, private_key[0], private_key[1])
    # assert x == y
    #
    # ints = file2ints("message.txt", 8)
    # for i in ints: print(i)

    import argparse

    parser = argparse.ArgumentParser(description="Fabians RSA Verschlüsselungs Tool")
    parser.add_argument("-l", "--loglevel", help="Set the logging level", default="WARNING",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR"], required=False)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-k", "--keygen", metavar="KEYGEN", help="generate new keys with the given length", type=int)
    group.add_argument("-e", "--encrypt", metavar="ENCRYPT", help="encrypt file", type=str)
    group.add_argument("-d", "--decrypt", metavar="DECRYPT", help="decrypt file", type=str)
    args = parser.parse_args()

    if args.loglevel:
        logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=args.loglevel)
        logger.setLevel(args.loglevel)

    if args.keygen:
        logger.info(f"Generating new keys with length {args.keygen}")
        generated_keys = generate_keys(args.keygen)
        save_keys(generated_keys)
        logger.info("Done generating keys")

    if args.encrypt:
        logger.info(f"Encrypting file: {args.encrypt}")
        encrypt_file(args.encrypt)
        logger.info("Done encrypting file. Output written to encrypted_message.txt")

    if args.decrypt:
        logger.info(f"Decrypting file: {args.decrypt}")
        decrypt_file(args.decrypt)
        logger.info("Done decrypting file. Output written to decrypted_message.txt")
