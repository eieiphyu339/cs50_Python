def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    bill_amount = 0
    try:
        while True:
            try:
                str = get_order("Item: ").title()
                if str in menu:
                    bill_amount += menu[str]
                    print(f"Total: ${bill_amount:.2f}")
                else: continue
            except(KeyError):
                pass
    except(EOFError):
        print("\nOrder Complete.")


def get_order(prompt):
    return input(prompt)

main()
