""" say yes if the user entered 42, forty two, or forty-two. or no otherwise"""


def main():
    print_ascii_art()
    ask()



def ask():
    while True:
        user_input = input("The answer to the Great Question of Life,"
        " the Universe and Everything: ").strip().lower()

        if user_input in ["42", "forty two", "forty-two", "fortytwo", "fortitude"]:
            
            print("YES!")
            break
        else:
            print("no...")


def print_ascii_art():
    set_color(34)  # Set color to blue
    print("   _______  ")
    print("  /       \\ ")
    print(" /  ^   ^  \\")
    print("|           |")
    print("|   \___/   |")
    print(" \\_________/ ")
    reset_color()

def set_color(color_code):
    print(f"\033[{color_code}m", end="")
def reset_color():
    print("\033[0m", end="")

main()