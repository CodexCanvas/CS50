"""" Promt the user for the name of a variable in camel case and
  output the name in snake case."""

snake_case = ""


def main():
    while True:
        camel_case = input("Enter a variable name in camel case: ")
        if camel_case == "":
            break
            exit()
        
        else:
            print(camel_to_snake(camel_case))
        
def camel_to_snake(camel_case):
    """Convert camel case to snake case."""
    global snake_case
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case


main()