import sys
import random
from pyfiglet import Figlet
import os

def main():
    figlet = Figlet()
    input_text = input("Input text: ")

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"]:
            try:
                figlet.setFont(font=sys.argv[2])
            except pyfiglet.FontNotFound:
                sys.exit(f"Error: Font '{sys.argv[2]}' not found.")
        else:
            sys.exit("Invalid argument. Use -f or --font to specify a font.")
    else:
        sys.exit("Invalid number of arguments. Use 0 or 2.")

    print(figlet.renderText(input_text))


def print_available_fonts():
    figlet = Figlet()
    fonts = figlet.getFonts()
    print("Available fonts:", ", ".join(fonts))


def welcome_message():
    print("Welcome to the Figlet program!")
    print("This program allows you to display text in various fonts.")
    print("You can choose a random font or specify a font using command-line arguments.")
    print("To specify a font, use -f or --font followed by the font name.")
    input("Press Enter to see the list of available fonts...")  # Pause


if __name__ == "__main__":
    welcome_message()
    print_available_fonts()
    main()