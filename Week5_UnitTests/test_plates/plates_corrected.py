""" prompt the user for a plate and then 
output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. """


def main():
    plate = input("Enter a license plate:").lower().strip()

    if  is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    return (starts_with_two_letters(plate) and
            correct_length(plate) and
            only_alphanumeric(plate) and
            first_number_not_zero(plate) and
            numbers_at_end(plate))


# All plates must start with at least two letters.
def starts_with_two_letters(plate):
    return len(plate) >= 2 and plate[0:2].isalpha()
# All plates must have between 2 and 6 characters.
def correct_length(plate):
    return 2 <= len(plate) <= 6
# No periods, spaces, or punctuation marks are allowed.
def only_alphanumeric(plate):
    return plate.isalnum()
# The first number used cannot be a 0
def first_number_not_zero(plate):
    for i in range(len(plate)):
        if plate[i].isdigit():
            if plate[i] == '0':
                return False
            else:
                break
    return True
# Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be acceptable; AAA22A would not be acceptable.
def numbers_at_end(plate):
    for i in range(len(plate)):
        if plate[i].isdigit():
            if not plate[i+1:].isdigit():
                return False
            else:
                break
    return True

if __name__ == "__main__":
    main()
