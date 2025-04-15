import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    try:
        number = int(sys.argv[1])

    except ValueError:
        raise AssertionError("argument is not an integer")

    if len(sys.argv) < 2:
        exit()
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(AssertionError.__name__ + ":", e)
    sys.exit(1)