# Ask user for their name and greet them
name = input("What is your name? ").strip().title()  # Strip leading and trailing whitespace

#split user input into first and last name
first_name, last_name = name.split()  # Split the name into first and last names



# Say hello to the user
print(f"Hello, {first_name}!")  # f-string for formatted string literals
