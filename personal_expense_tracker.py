# Expense Tracker Program
# This program allows users to track their expenses, set a monthly budget, and view their spending habits.

from datetime import datetime

def add_expense(expenses):
    try:
        while True:
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                # Validate date format
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter date as YYYY-MM-DD.")
        category = input("Enter the expense category: ")
        description = input("Enter the expense description: ")
        while True:
            amount_input = input("Enter the expense amount: ")
            try:
                amount = float(amount_input)
                if amount < 0:
                    print("Amount cannot be negative. Please enter a positive value.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        expense = {'description': description, 'amount': amount, 'date': date, 'category': category}
        expenses.append(expense)
        print("Expense added successfully!")
    except Exception as e:
        print(f"An error occurred while saving expense: {e}")
        

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet. Please add an expense first.")
        return
    # Read expenses from the expenses list
    try:
        for expense in expenses:
            print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']}, Category: {expense['category']}")
    
    except Exception as e:
        print(f"An error occurred while viewing expenses: {e}")

def set_monthly_budget():
    try:
        budget = float(input("Enter your total monthly budget: "))
        print(f"Monthly budget set to ${budget}")
        return budget
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return set_monthly_budget()

def calculate_total_expenses(expenses):
    total = 0.0
    for expense in expenses:
        total += expense.get('amount', 0.0)

    return total

def track_budget(expenses, budget):
    if budget <= 0:
        print("Please set a valid monthly budget first.")
        return
    if not expenses:
        print("No expenses recorded yet. Please add an expense first.")
        return
    total_expenses = calculate_total_expenses(expenses)
    print(f"Total expenses so far: ${total_expenses}")
    if total_expenses > budget:
        print("Warning: You have exceeded your budget!")
    else:
        remaining = budget - total_expenses
        print(f"You have ${remaining} left for the month.")

import csv

def save_expenses(expenses):
    if not expenses:
        print("No expenses to save.")
        return
    with open('expenses.csv', 'w', newline='') as csvfile:
        fieldnames = ['date', 'category', 'description', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow({
                'date': expense.get('date', ''),
                'category': expense.get('category', ''),
                'description': expense.get('description', ''),
                'amount': expense.get('amount', 0.0)
            })
    print("Expenses saved to expenses.csv")

import csv

def get_expenses_from_csv(filename='expenses.csv'):
    expenses = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                expense = {
                    'date': row.get('date', ''),
                    'category': row.get('category', ''),
                    'description': row.get('description', ''),
                    'amount': float(row.get('amount', 0.0))
                }
                expenses.append(expense)
    except FileNotFoundError:
        print(f"{filename} Not Found. Starting with an empty expense list.")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")
    return expenses

def main():
    expenses = get_expenses_from_csv()
    budget = 0
    while True:
        print("Welcome to Expense Tracker!")
        print("\nThis program will help you track your expenses.")
        print("\n1. Add an expense")
        print("\n2. View expenses")
        print("\n3. Track budget")
        print("\n4. Save expenses")
        print("\n5. Exit")

        choice = input("\nPlease enter your choice (1-5): ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            if budget == 0:
                budget = set_monthly_budget()
            track_budget(expenses,budget)
        elif choice == '4':
            save_expenses(expenses)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()