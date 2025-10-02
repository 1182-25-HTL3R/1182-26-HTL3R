__author__ = "Fabian Ha"

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Fabians RSA-Attack")
    parser.add_argument("-v", "--verbose", action="store_true", required=False, default=False)
    parser.add_argument("-m", metavar="MAX", required=False, type=int, action="store")
    parser.add_argument("modul", metavar="modul", required=True, type=int, action="store")
    args = parser.parse_args()

    N = args.modul
    p = None
    q = None
    attempts = None

