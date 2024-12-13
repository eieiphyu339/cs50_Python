import sys, csv

def main():
    inputfile = []
    firstname = ""
    lastname = ""
    if len(sys.argv)<3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv)>3:
        print("Too many command-line arguments")
        sys.exit(1)
    if not(sys.argv[1].endswith(".csv")) and not(sys.argv[2].endswith(".csv")):
        print("Not a csv file")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    lastname, firstname = row["name"].split(", ")
                    inputfile.append({"first":firstname, "last":lastname, "house":row["house"]})
                except KeyError:
                    print("Invalid csv format!")
                    sys.exit(1)

        with open(sys.argv[2], mode='w', newline='') as outputfile:
            writer = csv.DictWriter(outputfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(inputfile)
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)

if __name__ == "__main__":
    main()
