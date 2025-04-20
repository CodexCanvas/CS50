""" Prompt the user for a greeting and check if it starts with an h or not"""

def main():
    greeting = input("Greeting: ").strip().lower()
    if greeting == "hello":
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()