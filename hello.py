""" Ask user for their name and greet them """

name = None

# ANSI escape codes for changing text color
def set_color(color_code):
    print(f"\033[{color_code}m", end="")

# Reset to default color
def reset_color():
    print("\033[0m", end="")

# say_hello function that takes a name as input and prints a greeting message
def say_hello(to):
    print(f"Hello, {to} 😊")
    reset_color()

# Clean the name by removing any digits or special characters
def parse_name(name: str) -> str:
    # Define a function `parse_name` that takes a string `name` as input and returns a cleaned version of it.
    cleaned_name = ''
    # Initialize an empty string `cleaned_name` to store the cleaned version of the name.
    for char in name:
        # Iterate over each character in the input `name`.
        if char.isalpha() or char.isspace():
            # Check if the character is an alphabetic letter or a space.
            cleaned_name += char
            # If it is, append it to the `cleaned_name` string.
    return cleaned_name.title().strip()
    # Convert the cleaned name to title case (capitalize the first letter of each word),
    # remove any leading or trailing whitespace, and return the result.

# Change font color to blue
set_color(34)
print("   _______  ")
print("  /       \\ ")
print(" /  ^   ^  \\")
print("|           |")
print("|   \___/   |")
print(" \\_________/ ")
print("Hello world!")

# Keep asking for a name until the user enters one
while not name:
    name = input("What is your name?")
    if not name:
        print("You didn't enter a name!")

# Call the `parse_name` function with the user's input `name` and store the cleaned result in `parsed_name`.
parsed_name = parse_name(name)

# Split the cleaned name into words (using spaces as delimiters) and extract the first word (assumed to be the first name).
first_name = parsed_name.split()[0]

say_hello(first_name)
# Print a greeting message that includes the user's first name.