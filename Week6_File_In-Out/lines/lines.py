""" implement a program that expects exactly one command-line argument,
the name (or path) of a Python file,
and outputs the number of lines of code in that file,
excluding comments and blank lines.
If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .py,
or if the specified file does not exist,
the program should instead exit via sys.exit.

Assume that any line that starts with #,
optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.)
Assume that any line that only contains whitespace is blank. """

import sys

def main():
    check_command_line_arg()
    count = count_lines()
    print(count)


def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        return True


def count_lines():
    count = 0
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for line in lines:
                if line.lstrip().startswith("#"):
                    continue
                elif line.isspace():
                    continue
                else:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
    