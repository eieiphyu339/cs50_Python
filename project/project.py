import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os

def main():
    print("\nWelcome to Budget Tracker!")
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Analyze Spending\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_spending()
        elif choice == "4":
            print("Exiting from Budget Tracker ...")
            break
        else:
            print("Invalid choice. Please try again.")


def add_expense():
    date = input("Enter expense date (YYYY-MM-DD): ") or datetime.today().strftime('%Y-%m-%d')
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    description = input("Enter a short description: ")
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date,category,amount,description])
    print("Expense added successfully!")


def view_expenses():
    print("\nDate\t\tCategory\t\tAmout\t\tDescription")
    print("-" * 100)
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]}\t{row[1].ljust(24)}{row[2]}\t\t{row[3]}")
    except FileNotFoundError:
        print("No expenses found.")


def analyze_spending():
    categories = {}
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                categories[row[1]] = categories.get(row[1], 0) + float(row[2])
        if not categories:
            print("No spending data to analyze.")
            return

        labels = categories.keys()
        values = categories.values()

        plt.figure(figsize=(8,6))
        plt.pie(values, labels= labels, autopct='%1.1f%%', startangle=90)
        plt.title("Spending by category")
        plt.axis('equal')
        image_file = "expenses_analysis.png"
        plt.savefig(image_file)

        print("\nSpending analysis".ljust(33),"($)")
        print("-" * 36)
        grand_total = 0
        for category, total in categories.items():
            grand_total += total
            print(f"{category.ljust(24)}: {total:10.2f}")

        print("=" * 36)
        print(f"{grand_total:36.2f}")
        print("=" * 36)
        print(f"Pie chart saved as '{os.path.abspath(image_file)}'.")
        print("You can open the file in the VS Code file explorer or download it to view locally.")

    except FileNotFoundError:
        print("No expenses found.")


if __name__ == "__main__":
    main()
