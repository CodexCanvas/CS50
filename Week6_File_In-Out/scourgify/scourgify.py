"""Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input,
whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output,
whose columns should be, in order, first, last, and house.

Converts that input to that output,
splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments,
or if the first cannot be read, the program should exit via sys.exit with an error message."""

import sys
import csv



def main():
    check_csv_args()
    write_csv()

def check_csv_args():
    # check if there are exactly two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check if the first argument is a CSV file
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    # check if the second argument is a CSV file
    elif ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
    # check if the first argument exists
    else:
        return True

def write_csv():
    if check_csv_args() is True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                table = []
                for row in reader:
                    table.append(row)

                with open(sys.argv[2], "w") as file:
                    writer = csv.writer(file)
                    for row in table[1:]:
                        name = row[0].split(", ")
                        writer.writerow([name[1], name[0], row[1]])

        except FileNotFoundError:
            sys.exit("File does not exist")
            

if __name__ == "__main__":
    main()