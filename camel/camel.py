def main():
    str = input("camelCase: ")
    print("snake_case:", caseConvert(str))

def caseConvert(str):
    output = ""
    for c in str:
        if c.isupper():
            output += "_" + c.lower()
        else:
            output += c

    return output

if __name__ == "__main__":
    main()
