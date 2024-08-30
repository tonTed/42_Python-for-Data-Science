import sys


def string_stats(string: str):
    upper: int = 0
    lower: int = 0
    punctuation: int = 0
    digit: int = 0
    spaces: int = 0

    for c in string:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            spaces += 1
        else:
            punctuation += 1

    print(f"The text contains {len(string)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digit} digits")


def manage_input():
    """
    Manage the input from the user.
    """
    string = input("What is the text to count?\n")
    string_stats(string)


def main(argv):
    """
    Main function.

    Args:
        argv (list): List of arguments.

    Raises:
        AssertionError: If more than one argument is provided.
    """
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(argv) == 2 and argv[1] is not None:
        string_stats(argv[1])
    else:
        manage_input()


if __name__ == "__main__":
    main(sys.argv)
