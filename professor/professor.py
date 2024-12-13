import random

def main():
    trycount = 0
    score = 0
    problems = 0
    level = get_level()

    while problems < 10:
        a, b = generate_integer(level)
        ans = a + b

        for _ in range(3):
            try:
                input_ans = int(input(f"{a} + {b} = "))
                if input_ans == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    trycount += 1
            except(ValueError):
                trycount += 1
                print("EEE")

        if trycount == 3:
            print(f"{a} + {b} = {ans}")

        problems += 1
        trycount = 0

    print(f"Score = {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1,2,3]: return n
        except (ValueError): pass


def generate_integer(level):
    if level==3:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)
    elif level==2:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
    elif level==1:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

    return num1, num2

if __name__ == "__main__":
    main()
