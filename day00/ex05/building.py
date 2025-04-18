import sys
import string


def main():
    """ Count the number characters, upper case, lower case, punctuation,
    digits and spaces of the string give in argument to the program.
    Please provide only one string """
    try:
        if len(sys.argv) < 2 or sys.argv[1] is None:
            print("Please provide a string.")
            return
        if len(sys.argv) > 2:
            raise AssertionError("Too much arguments, please try again.")
        s = sys.argv[1]
        nOfChar = 0
        nOfUpper = 0
        nOfLower = 0
        nOfPunctuation = 0
        nOfSpace = 0
        nOfDigits = 0
        for c in s:
            nOfChar += 1
            if c.isupper():
                nOfUpper += 1
            elif c.islower():
                nOfLower += 1
            elif c in string.punctuation:
                nOfPunctuation += 1
            elif c.isspace():
                nOfSpace += 1
            elif c.isdigit():
                nOfDigits += 1
        print(f"The text contains {nOfChar} characters:")
        print(nOfUpper, "upper letters")
        print(nOfLower, "lower letters")
        print(nOfPunctuation, "punctuation marks")
        print(nOfSpace, "spaces")
        print(nOfDigits, "digits")

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
