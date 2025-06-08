""" expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate,
a package on PyPI at pypi.org/project/tabulate.
Format the table using the library’s grid format.
If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv,
or if the specified file does not exist,
the program should instead exit via sys.exit. """

import sys
import csv
from tabulate import tabulate

def main():
    check_csv()
    make_table()


def check_csv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        return True
    
def make_table():
    if check_csv() is True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                table = []
                for row in reader:
                    table.append(row)

                print(tabulate(table[1:], table[0], tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()