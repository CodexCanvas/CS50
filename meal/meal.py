""" Prompt the user for a time and output whether it is breakfast, lunch, or dinner time.
if the time is not in the range of any of the meals, do not output anything."""

print("   _______  ")
print("Welcome to the Meal Time Checker!")
print("Enter a time (HH:MM) ")


# prompt the user for a time, and output the corresponding meal for the corresponding hour range
def main():
    time = input("Current time?: ").strip()
    meal = get_meal(time)
    if meal:
        print(f"It's {meal} time!")
    else:
        exit()


def get_meal(time):
    # check if the time is in the range of breakfast, lunch, or dinner
    time = convert(time)
    if time is None:
        print("Please enter a valid time in HH:MM format.")
        return None
    if 7 <= time < 8:
        return "breakfast"
    
    elif 12 <= time < 13:
        return "lunch"
    
    elif 18 <= time < 19:
        return "dinner"
    
    return None


# convert time from a string to the corresponding time as a float
def convert(time):
    try:
        
        if "am" in time.lower() or "pm" in time.lower():
            time, period = time.lower().split()
            hours, minutes = map(int, time.split(":"))
            if period == "pm" and hours != 12:
                hours += 12
            elif period == "am" and hours == 12:
                hours = 0

        else:
            hours, minutes = map(int, time.split(":"))
        
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return hours + minutes / 60
        else:
            return None
    except ValueError:
        return None


# This block ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()