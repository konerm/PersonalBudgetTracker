Personal Budget Tracker

 Description

My Personal Budget Tracker is a Python application that helps users calculate their income, total expenses and remaining balance. I chose this project because budgeting is useful in everyday life and I struggle with it.

The program allows users to enter their income and multiple expenses. It then displays a budget summary.

Installation

1. Install Python.
2. Clone this GitHub repository.
3. Open the project folder in VS Code.
4. Install pytest using:

   python -m pip install pytest

Usage

Run the program in the terminal using:

    python main.py

Enter your income, the number of expenses and each expense amount.

Examples

Example 1: Income greater than expenses

    Total income: $3000.00
    Total expenses: $1500.00
    Remaining balance: $1500.00

Example 2: Expenses greater than income

    Total income: $1000.00
    Total expenses: $1500.00
    Remaining balance: $-500.00

Example 3: Invalid input

    Invalid input. Please enter numbers only.

 Testing

Run the five unit tests using:

    python -m pytest

GitHub Actions automatically runs the tests when changes are pushed to the repository.

Limitations

The program does not save previous budget information after it closes.
