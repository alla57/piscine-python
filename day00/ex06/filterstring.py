import sys
from ft_filter import ft_filter


def main():
    """This program accepts two arguments: a string S and an integer N.
    The program outputs a list of words from S that have a length
    greater than N
    Words should separated from each other by space characters.
    Strings do not contain any special characters. (Punctuation or invisible)
    If the number of argument is different from 2, or if the type
    of any argument is wrong, the program prints an AssertionError.
    Not respecting these rules could lead to unexpected behavior.
    """
    try:
        if len(sys.argv) != 3 or not isinstance(sys.argv[1], str):
            raise AssertionError()

        s = sys.argv[1].split()
        n = int(sys.argv[2])

        if not isinstance(n, int):
            raise AssertionError()

        it = ft_filter(lambda x: len(x) > n, s)
        print(list(it))

    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
