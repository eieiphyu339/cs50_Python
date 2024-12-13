import inflect, sys

def main():
    names = []
    inflect_eng = inflect.engine()
    try:
        while True:
            name = input("Name: ")
            names.append(name)

    except (EOFError):
        print()
        farewell = f"Adieu, adieu, to {inflect_eng.join(names)}"
        print(farewell)


if __name__ == '__main__':
    main()
