import sys


def string_stats(string: str):
    """
    Print the stats of the string.

    Args:
        string (str): The string to count.
    """
    print(f"The text contains {len(string)} characters:")


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
    if len(argv) == 2:
        string_stats(argv[1])
    else:
        manage_input()


if __name__ == "__main__":
    main(sys.argv)
