def main():
    # Prompts the user for a greeting and prints the corresponding value.
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")


def value(greeting):
    # Calculates the value based on the greeting.
    if greeting == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    elif greeting == "":
        exit()
        
    else:
        return 100


if __name__ == "__main__":
    main()