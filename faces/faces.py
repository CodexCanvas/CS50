""" detect any :) and :( in the user input and replace them with the corresponding emojis"""


def main ():
    user_input = input("Enter a string with :) or :( : ")
    converted_input = convert(user_input)
    print("Converted string:", converted_input)

def convert(input:str) -> str:
    return input.replace(':)', '😊').replace(':(', '😞')


main()