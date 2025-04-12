""" Ask the user for a number and print the square of that number """

# Don't do this:
# print(int(input("What's X? ")) + int(input("What's Y? ")))

def main():
    n = None
    while n== None:
        try:
            n = int(input("What's n? "))
        except ValueError:
            print("Please enter a valid number.")
    print(f"{n} squared is", square(n))

def square(n):
    return n * n

main()


# while True:
#     x = input("What's X? ")
#     y = input("What's Y? ")
#     # Check if the inputs are numbers
#     try:
#         x = float(x)
#         y = float(y)
#         break  # Exit the loop if inputs are valid
#     except ValueError:
#         print("Please enter valid numbers.")

# # z = round(x / y, 2) # Round the result to two decimal places

# print(f"{z:,}")


# z = round(x + y) # Round the sum to two decimal places