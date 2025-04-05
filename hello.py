""" Ask user for their name and greet them """


name = None


# Keep asking for a name until the user enters one
while not name:
    name = input("What is your name? ")
    if not name:
        print("You didn't enter a name!")


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


parsed_name = parse_name(name)
# Call the `parse_name` function with the user's input `name` and store the cleaned result in `parsed_name`.

first_name = parsed_name.split()[0]
# Split the cleaned name into words (using spaces as delimiters) and extract the first word (assumed to be the first name).

print(f"Hello, {first_name}!")
# Print a greeting message that includes the user's first name.