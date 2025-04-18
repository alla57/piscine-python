import sys


def main():
    """Morse Code Encoder Program

    This script takes a single string as a command-line argument
    and encodes it into Morse code.

    Features:
    - Supports alphanumeric characters (A-Z, 0-9) and spaces.
    - Morse code characters are separated by a single space.
    - Spaces between words are represented by a slash (/).
    - The program is case-insensitive (i.e., 'a' and 'A' are treated the same).

    Usage:
        python3 sos.py "Your message here"

    Example:
        python3 sos.py "Hello World"
        Output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

    Constraints:
    - Exactly one argument must be provided.
    - If the number of arguments is not 1 or the argument is not a string, or
    contains unhandled characters, an AssertionError is raised.
    """
    morseDict = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        ' ': '/'}

    try:
        if len(sys.argv) != 2:
            raise AssertionError("Wrong number of arguments")
        if not isinstance(sys.argv[1], str):
            raise AssertionError("Wrong type of arguments")
        for c in sys.argv[1]:
            if not c.isalnum():
                if c != ' ':
                    raise AssertionError("Characters not supported! \
                    Please use only Alphanumeric and space characters")

        morseInput = sys.argv[1].upper()
        translated = [morseDict[c] for c in morseInput]
        res = ' '.join(translated)
        print(res)

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
