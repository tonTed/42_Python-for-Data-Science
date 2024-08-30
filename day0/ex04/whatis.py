import sys


def whatis():
    if len(sys.argv) == 1:
        return
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        number = int(sys.argv[1])
        print("I'm Even." if number % 2 == 0 else "I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    whatis()
