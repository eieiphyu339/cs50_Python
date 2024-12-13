import emoji

def main():
    str = input("Input: ")

    print(emoji.emojize(f"Python is fun :{str}", language='alias'))


main()

