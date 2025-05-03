""" prompts the user for a date, anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list 
Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format,
prompt the user again. Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days."""

# List of month names.  Used for converting month names to numbers.
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        # Prompt the user to enter a date.
        date_input = input("Enter a date (MM/DD/YYYY or Month DD, YYYY):")
        # Use a try-except block to handle potential errors during date processing.
        try:
            # Check if the date is in MM/DD/YYYY format.
            if '/' in date_input:
                # Split the date string into month, day, and year using '/' as the delimiter.
                month, day, year = map(int, date_input.split('/'))
                # Check if the month, day, and year are within valid ranges.
                if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                    # Print the date in YYYY-MM-DD format.  :04d, :02d ensure padding with zeros.
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    # Break out of the loop if the date is valid.
                    break
            # If the date is not in MM/DD/YYYY format, assume it's in Month DD, YYYY format.
            else:
                # Split the date string into month and day/year parts, splitting at the first space.
                month_str, day_year = date_input.split(' ', 1) 
                # Find the index of the month in the months list and add 1 to get the month number.
                month = months.index(month_str) + 1
                # Split the day and year part, removing leading/trailing whitespace and splitting at the ','.
                day, year = map(int, day_year.strip().split(',')) 
                # Check if the month, day, and year are within valid ranges.
                if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                    # Print the date in YYYY-MM-DD format.
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    # Break out of the loop if the date is valid.
                    break
        # Handle ValueError (if conversion to integer fails) and IndexError (if month is not found).
        except (ValueError, IndexError):
            print("Invalid date format. Please try again.")

main()