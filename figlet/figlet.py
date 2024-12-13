from pyfiglet import Figlet
import sys

def main():
    figlet = Figlet()

    try:
        if (len(sys.argv)==3):
            if sys.argv[1] == "--font" or sys.argv[1] == "-f":
                f = sys.argv[2]
                try:
                    figlet.setFont(font=f)
                except (FontNotFound):
                    sys.exit(1)
            else:
                print("Invalid usage")
                sys.exit(1)
        elif (len(sys.argv)==2): sys.exit(1)

        str = input("Input: ")
        print("Output: ")
        print(figlet.renderText(str))

    except (NameError):
        print("Invalid font")
        sys.exit(1)

main()
