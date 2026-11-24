def calculate_balance(income, expenses):
    """Calculate the remaining balance."""
    return income - expenses


def calculate_expenses(expenses):
    """Calculate the total expenses."""
    return sum(expenses)


def main():
    print("Welcome to Personal Budget Tracker")
    income = float(input("Enter your income: "))
    expenses = []
    num_expenses = int(input("How many expenses do you have? "))

    for i in range(num_expenses):
        expense = float(input("Enter expense amount: "))
        expenses.append(expense)

    total_expenses = calculate_expenses(expenses)
    balance = calculate_balance(income, total_expenses)

    print("Budget Summary")
    print(f"Total income: ${income:.2f}")
    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Remaining balance: ${balance:.2f}")


if __name__ == "__main__":
    main()