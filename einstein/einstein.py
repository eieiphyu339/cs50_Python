def ans(mass):
    return(int(mass*pow(300000000,2)))

def main():
    mass = input("m : ")
    print(f"{ans(int(mass)):,}")

main()
