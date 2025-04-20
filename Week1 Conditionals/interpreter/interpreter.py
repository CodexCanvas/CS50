""" prompt the user for an arithmetic expression and output the result """

def main():

    set_color(32)  # Set color to green
    print("""
         A       EEEEE   IIIII
        A A      E         I  
       A   A     EEEE      I  
      AAAAAAA    E         I  
     A       A   EEEEE   IIIII
        """)
    print("Welcome to the Arithmetic Expression Interpreter!")
    print("enter 'EXIT' to quit the interpreter")
    reset_color()
    print()
    print("Enter an arithmetic expression:")

    while True:
        try:
            expression = input("> ")
            result = round(float(eval(expression)), 1)
            print(f"🤖 -|The result is {result} ")
            print()
        except Exception as e:
            print(f"💥 Error : {e}")
        if expression.lower() == "exit":
            print("Exiting the interpreter.")
            break


def set_color(color_code):
    print(f"\033[{color_code}m", end="")
def reset_color():
    print("\033[0m", end="")

main()