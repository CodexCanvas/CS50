""""  place an order, prompting them for items, one per line,
until the user inputs control-c. After each inputted item, 
display the total cost of all items inputted thus far,
prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item.
Assume that every item on the menu will be titlecased. """

import sys

menu = {
    "Baja Tacos": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Qusadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Qusadilla": 9.50,
    "Tacos": 3.00,
    "Tortilla Salad": 8.00
}

print("Baja Tacos: 4.25\n"
    "Burrito: 7.50\n"
    "Bowl: 8.50\n"
    "Nachos: 11.00\n"
    "Qusadilla: 8.50\n"
    "Super Burrito: 8.50\n"
    "Super Qusadilla: 9.50\n"
    "Tacos: 3.00\n"
    "Tortilla Salad: 8.00")


def main():
    total_cost = 0.0
    while True:
        try:
            item = input("Enter an item (or press Ctrl-C to finish): ").strip()
            if not item:
                continue
            item_cost = menu.get(item.title())
            if item_cost is not None:
                total_cost += item_cost
                print(f"${total_cost:.2f}")
            else:
                print(f"'{item}' is not on the menu.")
        except KeyboardInterrupt:
            print("\nOrder completed.")
            print(f"Total cost: ${total_cost:.2f}")
            break





main()