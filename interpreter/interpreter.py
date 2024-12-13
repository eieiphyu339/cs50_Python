def main():
    str_exp = input("Expression: ").strip()

    x, y, z = str_exp.split(" ")

    match y:
        case "+": print(float(x)+float(z))
        case "-": print(float(x)-float(z))
        case "*": print(float(x)*float(z))
        case "/": print(float(x)/float(z))

main()
