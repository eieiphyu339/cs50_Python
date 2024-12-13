def main():
    str = input("Input: ")
    print("Output:", shorten(str))

def shorten(word):
    output = ""
    for c in word:
        if (c.lower() in ["a","e","i","o","u"])==0:
            output += c

    return output

if __name__ == "__main__":
    main()
