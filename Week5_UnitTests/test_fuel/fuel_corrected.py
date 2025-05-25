def main():
    while True:
        try:
            # Prompt the user for a fraction
            fraction = input("Enter a fraction (X/Y): ")
            percentage = convert(fraction)
            output = gauge(percentage)
            print(output)
            break  # Exit the loop if everything is valid
        except (ValueError, ZeroDivisionError):
            print(" Enter a valid fraction: ")

def convert(fraction):
    # Convert the fraction X/Y to a percentage
    x, y = map(int, fraction.split('/'))
    if y == 0 or x > y:
        raise ValueError("Invalid fraction.")
    return (x / y) * 100

def gauge(percentage):
    # Determine the output based on the percentage
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"  # Return as string with percentage symbol

if __name__ == "__main__":
    main()