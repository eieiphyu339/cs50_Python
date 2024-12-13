from datetime import date
import inflect
import sys

def main():
    birth_date = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")

    today_date = date.today()
    age_in_minutes = calculate_age_in_minutes(birth_date, today_date)
    age_in_words = convert_to_words(age_in_minutes)
    print(f"{age_in_words} minutes")

def calculate_age_in_minutes(b_date, today):
    difference_in_days = (today - b_date).days
    total_minutes = difference_in_days * 24 * 60
    return total_minutes

def convert_to_words(minutes):
    if not isinstance(minutes, int):
        raise ValueError("Minutes should be an integer")

    narration = inflect.engine()
    words = narration.number_to_words(minutes, andword="")
    return words.capitalize()


if __name__ == "__main__":
    main()
