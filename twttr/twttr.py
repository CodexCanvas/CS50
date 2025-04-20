""" prompts the user for a str of text and then 
outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase. """

def main():
    while True:
        # Prompt the user for a string of text
        text = input("Twtt: ")
        
        # Check if the input is empty
        if not text or text.lower() == "exit":
            print("Goodbye!")
            exit()
        
        # Define the vowels to be omitted
        vowels = "aeiouAEIOU"
        
        # Omit the vowels from the text
        no_vowels_text = "".join([char for char in text if char not in vowels])
        
        # Output the modified text
        print(no_vowels_text)
        
    

main()