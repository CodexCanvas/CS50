def main():
    names = []
    print("Enter names, one per line (blank line to finish):")
    while True:
        name = input()
        if not name:  # Check for a blank line
            break
        names.append(name)

    if not names: #Handle case where no names are entered
        print("No names entered.")
        return

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    elif len(names) == 3:
        print(f"Adieu, adieu, to {names[0]}, {names[1]}, and {names[2]}")
    else:
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")


if __name__ == "__main__":
    main()