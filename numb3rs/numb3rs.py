import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if not match:
        return False

    for group in match.groups():
        if not 0 <= int(group) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()
