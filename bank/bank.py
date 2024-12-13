import sys

def main():
    str = input("Greeting: ")
    print(f"${value(str)}")

def value(greeting):
    greeting = greeting.lower()

    # if greeting.startswith("hello"):
    #     return 0
    # elif greeting.startswith("h"):
    #     return 20
    # else:
    #     return 100

    if len(greeting)>0:
        if greeting[0].isdigit()==False:
            if greeting.startswith("hello"):
                return 0
            elif greeting.startswith("h"):
                return 20
            else:
                return 100
        else:
            return ""
    else:
        return 100

if __name__ == "__main__":
    main()
