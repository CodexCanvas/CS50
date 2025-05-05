"""Prompts the user for a level, 'n'.
If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 'n', inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer,
the program should prompt the user again.
If the guess is smaller than that integer,
the program should output Too small! and prompt the user again.
If the guess is larger than that integer,
the program should output Too large! and prompt the user again.
If the guess is the same as that integer,
the program should output Just right! and exit. """

import random

def main():
    #Prompt the user for a level, 'n'.
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass

    #Randomly generates an integer between 1 and 'n', inclusive, using the random module.
    secret = random.randint(1, n)
    while True:
        #Prompts the user to guess that integer.
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue
        
        #if the guess is smaller than that integer,
        #the program should output Too small! and prompt the user again.
        if guess < secret:
            print("Too small!")
        #If the guess is larger than that integer,
        #the program should output Too large! and prompt the user again.
        elif guess > secret:
            print("Too large!")
        #If the guess is the same as that integer,
        #the program should output Just right! and exit.
        else:
            print("Just right!")
            break
    

if __name__ == "__main__":
    main()