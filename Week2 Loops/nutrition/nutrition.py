"""prompts users to input a fruit (case-insensitively) and then
outputs the number of calories in one portion of that fruit, as per the dictionary.
Capitalization aside, assume that users will input fruits exactly as written in the dictionary.
Ignore any input that is not a fruit. """

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew_melon" : 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear" : 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet_cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

def main():
    fruit = input("Enter a fruit:").strip().lower()

    if fruit in fruits:
        calories = fruits[fruit]
        print(f"{fruit.capitalize()}'s have {calories} KCal.")



main()