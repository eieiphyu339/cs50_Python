#### Title: Budget Tracker

#### Video Demo: [https://youtu.be/OoLA7264ahE]

#### Overview:
Budget Tracker is a Python program that helps users manage their personal finances by tracking income and expenses.
It allows users to add, view, and categorize transactions, and view summaries.

#### Features:
- Add income or expense entries.
- Categorize transactions (e.g., food, transportation, etc,).
- View summaries by category.
- Error handling for invalid inputs.

#### Description:
Budget Tracker is a simple Python program that helps users manage their daily expenses.
Users can:
1. Add new expenses with details like date, category, amount, and description.
2. View a summary of all recorded expenses in a tabular format.
3. Analyze spending by generating a pie chart of expenses by category.

#### File Descriptions:
- 'project.py' : Contains the main application logic, including 'add_expense', 'view_expenses'
    and 'analyze_spending' functions.
- 'test_project.py' : Contains unit tests for the key functions of the project.
- 'requirements.txt' : Lists external dependencies (e.g., 'matplotlib').

#### Usage Instructions:
1. Clone the repository or download the 'project.py' file.
2. Run the program with 'python project.py'.
3. Follow the on-screen prompts to interact with the program.

#### Example usage:
Welcome to Budget Tracker!
1. Add Expense
2. View Expenses
3. Analyze Spending
4. Exit
1
Enter expense date (YYYY-MM-DD): 2024-12-10
Enter expense category: Food
Enter expense amount: 3
Enter a short description: Buying snacks
Expense added successfully!

#### Future Improvements:
- Add a graphical user interface (GUI).
- Implement data export to CSV or JSON.

#### Challenges:
One challenge was ensuring the pie chart accurately reflected expense categories.
Another was designing test cases for user inputs using 'pytest'.
