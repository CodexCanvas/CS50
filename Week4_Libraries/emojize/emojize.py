"""Prompt the user for a string in English
and then outputs the “emojized”version of that string.
This function converts any emoji codes (or aliases)
in the input string to their corresponding emoji."""

import emoji


def emojize_string(input_string: str) -> str:
    return emoji.emojize(input_string, language="alias")


def main():
    user_input = input("Enter a emoji code:")
    emojized_string = emojize_string(user_input)
    print(f"Emojized string: {emojized_string}")


main()
