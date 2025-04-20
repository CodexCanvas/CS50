""" set any user input to lowercase """

shout : str 

def main():
    # Get user input
    shout = get_input(":> ")
    
    # Convert to lowercase
    lowercase_string = set_lowercase(shout)
    
    # Print the result
    print_string(lowercase_string)
   
    

def get_input(prompt: str) -> str:
    return input(prompt)


def set_lowercase(string: str) -> str:
    return string.lower()
    

def print_string(string: str):
    print(string)
    

main()