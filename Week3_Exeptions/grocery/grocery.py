""" prompts the user for items, one per line,
until the user inputs control-c.
Then output the user’s grocery list in all uppercase,
sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items.
Treat the user’s input case-insensitively. """

def main():
    # Initialize an empty dictionary to store grocery items and their counts.
    grocery_list = {}
    # Prompt the user to enter grocery items, indicating how to finish input.
    print("Enter grocery items (Ctrl+C to finish): ")

    # Use a try-except block to handle the KeyboardInterrupt exception when Ctrl+C is pressed.
    try:
        # Start an infinite loop that continues until Ctrl+C is pressed.
        while True:
            # Read a line of input from the user, remove leading/trailing whitespace.
            item = input().strip()
            # Check if the input is not empty.
            if item:
                # Convert the item to uppercase for case-insensitive comparison.
                item_upper = item.upper()
                # Check if the item already exists in the grocery list.
                if item_upper in grocery_list:
                    # If the item exists, increment its count.
                    grocery_list[item_upper] += 1
                else:
                    # If the item doesn't exist, add it to the list with a count of 1.
                    grocery_list[item_upper] = 1
    # Handle the KeyboardInterrupt exception (Ctrl+C) gracefully, ignoring it.
    except KeyboardInterrupt:
        pass

    # Sort the grocery list items alphabetically.
    sorted_items = sorted(grocery_list.items())

    # Print a header for the grocery list.
    print("\nYour grocery list:")
    # Iterate through the sorted items and print each item and its count.
    for item, count in sorted_items:
        print(f"{count} {item}")
    


# Call the main function to execute the program.
main()