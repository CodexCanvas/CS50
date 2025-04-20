""" prompt the user to insert a coin, one at a time,
    each time informing the user of the amount due.
    Once the user has inputted at least 50 cents,
    output how many cents in change the user is owed.
    Assume that the user will only input integers,
    and ignore any integer that is not an accepted denomination. """
def main():
    # Define the denominations
    denominations = [5, 10, 25, 50]
    amount_entered = 0
    
    while amount_entered < 50:
        # Prompt the user for a coin
        coin = int(input("Insert a coin: "))
        # Check if the coin is valid
        if coin in denominations:
            amount_entered += coin
            if amount_entered > 50:
                print(f"Change owed: {amount_entered - 50} cents")
            elif amount_entered == 50:
                print("Thank you!")
            else:
                print(f"Amount due: {50 - amount_entered} cents")
        else:
            print("Invalid coin. Please insert a valid denomination.")
main()