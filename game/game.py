import random, sys

def main():
    try:
        while True:
            try:
                n = int(input("Level: "))
                rnd = random.randrange(1, n+1)
                guess = int(input("Guess: "))
                if (guess>rnd): print("Too large!")
                elif (guess<rnd): print("Too small!")
                else:
                    print("Just right!")
                    sys.exit(1)
            except (ValueError): continue
    except (EOFError): pass



if __name__ == '__main__':
    main()
