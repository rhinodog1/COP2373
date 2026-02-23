from functools import reduce

def get_expenses():
    """
    Prompts the user to input their monthly expenses.
    Returns a list of dictionaries, each containing 'type' and 'amount'.
    """
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append({"type": expense_type, "amount": amount})
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")
    return expenses

def calculate_total(expenses):
    """
    Calculates the total of all expenses using reduce.
    """
    return reduce(lambda acc, x: acc + x['amount'], expenses, 0)

def find_highest(expenses):
    """
    Finds the expense with the highest amount.
    """
    return reduce(lambda x, y: x if x['amount'] > y['amount'] else y, expenses)

def find_lowest(expenses):
    """
    Finds the expense with the lowest amount.
    """
    return reduce(lambda x, y: x if x['amount'] < y['amount'] else y, expenses)

def main():
    print("Welcome to the Monthly Expenses Tracker!")
    expenses = get_expenses()

    if not expenses:
        print("No expenses were entered.")
        return

    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    print("\nExpense Summary:")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest['type']} - ${highest['amount']:.2f}")
    print(f"Lowest Expense: {lowest['type']} - ${lowest['amount']:.2f}")

if __name__ == "__main__":
    main()