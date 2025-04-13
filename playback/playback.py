"""  replace every space in a string with ... """


#SPARTA!!!
def main():
    # Get user input
    input_string = input(":> ")
    
    # Replace spaces with '...'
    modified_string = input_string.replace(" ", "...")

    # Print the result in all caps
    print(f"{modified_string.upper()}!!!")


main()
