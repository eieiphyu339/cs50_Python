import sys

def main():
    lines = 0
    if len(sys.argv) != 2:
        sys.exit(1)

    if not(sys.argv[1].endswith(".py")):
        print("File must have a .py extension.")
        sys.exit(1)
        
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                row = line.lstrip()
                if not(row.startswith("#")) and not(len(row)==0):
                    lines += 1
        print(lines)
    except FileNotFoundError:
        print("File not found!!")

if __name__ == "__main__":
    main()
