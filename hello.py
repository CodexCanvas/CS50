""" Ask user for their name and greet them """

def main():
    print_ascii_art()
    name = get_name()
    parsed_name = parse_name(name)
    first_name = parsed_name.split()[0]
    say_hello(first_name)

# ANSI escape codes for changing text color
def set_color(color_code):
    print(f"\033[{color_code}m", end="")

# Reset to default color
def reset_color():
    print("\033[0m", end="")

# say_hello function that takes a name as input and prints a greeting message
def say_hello(to):
    print(f"Hello, {to} 🤖")
    reset_color()

# Clean the name by removing any digits or special characters
def parse_name(name: str) -> str:
    # Define a function `parse_name` that takes a string `name` as input and returns a cleaned version of it.
    cleaned_name = ''
    # Initialize an empty string `cleaned_name` to store the cleaned version of the name.
    for char in name:
        if char.isalpha() or char.isspace():
            cleaned_name += char
    return cleaned_name.title().strip()

# Function to print the ASCII art
def print_ascii_art():
    set_color(34)  # Set color to blue
    print("   _______  ")
    print("  /       \\ ")
    print(" /  ^   ^  \\")
    print("|           |")
    print("|   \___/   |")
    print(" \\_________/ ")
    print("Hello world!!")
    reset_color()

# Ask the user for their name until a valid name is provided
def get_name():
    name = None
    while not name:
        name = input("What is your name? ")
        if not name:
            print("You didn't enter a name!")
    return name

main()