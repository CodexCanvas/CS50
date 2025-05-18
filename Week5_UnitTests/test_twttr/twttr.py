""" prompts the user for a str of text and then 
outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase. """

def shorten(text):
    if not text:  # Handle empty input
        return ""

    vowels = "aeiou"
    no_vowels_text = "".join([char for char in text if char not in vowels])
    return no_vowels_text


def main():
    while True:
        text = input("Twtt: ")
        if not text or text.lower() == "exit":
            print("Goodbye!")
            break  # Use break to exit the loop cleanly

        result = shorten(text)
        if result is not None:  #Check for invalid input from shorten()
            print(result)


if __name__ == "__main__":
    main()