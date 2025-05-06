""" Prompt the user for a level,'n'.
If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with 'n' digits.
No need to support operations other than addition (+).
Prompts the user to solve each of those problems.
If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again,
allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries,
the program should output the correct answer.
The program should ultimately output the user’s score:
the number of correct answers out of 10.
Structure your program as follows,
wherein get_level prompts (and, if need be, re-prompts)
the user for a level and returns 1, 2, or 3,
and generate_integer returns a randomly generated non-negative integer with level digits
or raises a ValueError if level is not 1, 2, or 3: """



import random


def main():
    # Prompt the user for a level, 'n'.
    Level = get_level()
    # Randomly generates ten math problems formatted as X + Y = ,
    # wherein each of X and Y is a non-negative integer with 'n' digits.
    score = 0
    for i in range(10):
        x = generate_integer(Level)
        y = generate_integer(Level)
        answer = x + y
        # Prompts the user to solve each of those problems.
        for j in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                continue
        else:
            print(f"{x} + {y} = {answer}")
    # The program should ultimately output the user´s score:
    # the number of correct answers out of 10.
    print(f"Score: {score}/10")

    return score


    


def get_level():
    # Prompt the user for a level, 'n'.
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass
    # If the user does not input 1, 2, or 3, the program should prompt again.

    


def generate_integer(level):
    # Randomly generates a non-negative integer with level digits.
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()