# Ask the user for two numbers and print their sum
while True:
    x = input("What's X? ")
    y = input("What's Y? ")

    # Check if the inputs are numbers
    try:
        x = float(x)
        y = float(y)
        break  # Exit the loop if inputs are valid
    except ValueError:
        print("Please enter valid numbers.")

z = round(x / y, 2)


# z = round(x + y) # Round the sum to two decimal places


print(f"{z:,}")


# Don't do this:
# print(int(input("What's X? ")) + int(input("What's Y? ")))