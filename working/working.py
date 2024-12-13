import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?:(\d{1,2}):?(\d{2})? (AM|PM)) to (?:(\d{1,2}):?(\d{2})? (AM|PM))$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    if start_minute: start_minute = int(start_minute)
    else: start_minute = int(0)

    if end_minute: end_minute = int(end_minute)
    else: end_minute = int(0)

    start_24 = to_24_hour(int(start_hour), start_minute, start_period)
    end_24 = to_24_hour(int(end_hour), end_minute, end_period)

    return f"{start_24} to {end_24}"

def to_24_hour(hour, minute, period):
    if not (1<=hour<=12) or not (0<= minute <=60):
        raise ValueError("Invalid time value")

    if period=="PM" and hour!=12:
        hour += 12
    elif period=="AM" and hour==12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
