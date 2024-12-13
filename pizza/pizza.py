import sys, csv

from tabulate import tabulate

def main():
    if (len(sys.argv)<2):
        print("Too few command-line arguments")
        sys.exit(1)
    if (len(sys.argv)>2):
        print("Too many command-line arguments")
        sys.exit(1)

    if not(sys.argv[1].endswith(".csv")):
        print("Given non-csv file")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = [row for row in reader]

            table = tabulate(rows, headers=header, tablefmt="grid")
            print(table)
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)

if __name__ == "__main__":
    main()
