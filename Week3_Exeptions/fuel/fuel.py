"""" prompt the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then
outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank. 
If, though, 1% or less remains, output E instead 
to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead
to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead
prompt the user again. (It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError. """


def main():
    while True:
        try:
            # Prompt the user for a fraction
            fraction = input("Enter a fraction (X/Y): ")
            x, y = map(int, fraction.split('/'))

            # Check if Y is 0 or if X is greater than Y
            if y == 0 or x > y:
                raise ValueError("Invalid fraction.")
                
            # Calculate the percentage of fuel in the tank
            percentage = (x / y) * 100
            # Determine the output based on the percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(round(percentage))

            break # Exit the loop if everything is valid
        except (ValueError, ZeroDivisionError):
            print(" Enter a valid fraction: ")

main()