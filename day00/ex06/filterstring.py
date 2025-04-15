import sys
from ft_filter import ft_filter

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1].split()
        n = int(sys.argv[2])

        if not isinstance(s, str) or not isinstance(n, int)
            raise AssertionError("the arguments are bad")

        it = ft_filter(lambda x : len(x) > n, s)
        print(list(it))

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__=="__main__":
    main()