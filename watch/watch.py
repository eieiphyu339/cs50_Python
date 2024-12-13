import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # match = re.search(r'src=\"https?://(?:www\\.)?youtube\\.com/embed/([\\w-]+)\"', s)
    # match = re.search(r'HTML: <iframe[^>]*src=\"https?://(?:www\\.)?youtube\\.com/embed/([\\w-]+)\"', s, re.IGNORECASE)

    pattern = r'<iframe[^>]*src=\"https?://(?:www\.)?youtube\.com/embed/([\w-]+)\"'
    match = re.search(pattern, s, re.IGNORECASE)

    # print(pattern)
    # print(f"Match object: {match}")

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
