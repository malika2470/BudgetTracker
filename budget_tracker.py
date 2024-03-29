import matplotlib.pyplot as plt
import pandas as pd
from inquirer import prompt

def add_income(income_data):
    questions = [
        {
            'type': 'input',
            'name': 'income',
            'message': 'Enter income amount:',
            'validate': lambda val: val.replace('.', '', 1).isdigit()  # Validate if input is a positive number
        },
        {
            'type': 'input',
            'name': 'category',
            'message': 'Enter income category:',
        }
    ]

    answers = prompt(questions)
    income = float(answers['income'])
    category = answers['category']
    income_data.append({"Category": category, "Amount": income})

def add_expense(expense_data):
    questions = [
        {
            'type': 'input',
            'name': 'expense',
            'message': 'Enter expense amount:',
            'validate': lambda val: val.replace('.', '', 1).isdigit()  # Validate if input is a positive number
        },
        {
            'type': 'input',
            'name': 'category',
            'message': 'Enter expense category:',
        }
    ]

    answers = prompt(questions)
    expense = float(answers['expense'])
    category = answers['category']
    expense_data.append({"Category": category, "Amount": expense})

def generate_report(income_data, expense_data):
    income_df = pd.DataFrame(income_data)
    expense_df = pd.DataFrame(expense_data)

    total_income = income_df["Amount"].sum()
    total_expense = expense_df["Amount"].sum()

    print("\n---- Income Report ----")
    print(income_df)
    print("\n---- Expense Report ----")
    print(expense_df)
    print("\nTotal Income: $", total_income)
    print("Total Expense: $", total_expense)
    print("Net Income: $", total_income - total_expense)

    # Visualize data
    combined_df = pd.concat([income_df, expense_df])
    grouped_df = combined_df.groupby("Category")["Amount"].sum()
    grouped_df.plot(kind="bar")
    plt.title("Budget Categories")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def main():
    income_data = []
    expense_data = []

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_income(income_data)
        elif choice == "2":
            add_expense(expense_data)
        elif choice == "3":
            generate_report(income_data, expense_data)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    //
