import time


def add_expense(data):
    category_list = ['Food', 'Transportation', 'Entertainment', 'Sports', 'Home', 'Others']

    while True:
        try:
            date = get_date_input()
            date_timestamp = time.mktime(date.timetuple())

            category = input(
                "Enter Category (e.g., Food, Transportation, Entertainment, Sports, Home, Others): ").capitalize()
            if category not in category_list:
                print("Category not found")
                return False

            amount = int(input("Please input the Amount: "))
            if amount < 0:
                raise ValueError

            description = input("Please write a brief Description: ")
            break

        except ValueError:
            print("Amount should be a positive number")
            print("Please Try Again")

    new_expense = {
        'category': category,
        'amount': amount,
        'date': date_timestamp,
        'description': description
    }
    if isinstance(data, list):
        data.append(new_expense)
    else:
        data = [new_expense]

    print(new_expense)
    print(f"\nExpense added successfully: Spent {amount} on {category} on {date.strftime('%Y-%m-%d')}\n")

    return data

def view_expense(data):
    if not data:
        print("\nNo Data Found \n ")
        return
    total = 0
    print("      1 - View All Expenses ")
    print("      2 - to View Expense by Category")
    print("      3 - to View Expense by date")
    choice = input("     Enter your Choice: ")
    if choice == '1':
        print(data)
        print('Date          Expenses             Category                Description')
        for key in data:
            total += int(key['amount'])
            print(f"{key['date']:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")
        print('-' * 56)
        print(f"\nYour Overall Expense is: {total} \n")
    elif choice == '2':
        k = 1
        for key in data:
            print(f'{k}: {key["category"]}')
            k += 1
        cat = input("If you want to calculate expense by category then enter category name: ")
        cat_total = 0
        for key in data:
            if key['category'] == cat.capitalize():
                cat_total += key['amount']

        print(f'Overall Expense of {cat} Category is {cat_total}')
    elif choice == '3':
        print("If you want to calculate expense by Date then enter Date : ")
        date = get_date_input()
        date = time.mktime(date.timetuple())

        print('Category          Expenses             Description ')
        for key in data:
            if key['date'] == date:
                print(key['category'],"           ",    key['amount'],"                ",key['description'])

    else:
        print(" Invalid Choice")

def delete_expense(data):
    k=1
    for key in data:
        print(f'{k}: {key["category"]}')
        k +=1
    name = input("\nPlease Select a Category which you want to delete: ")

    for key in data:
        if key['category'] == name.capitalize():
            confirm = input("Press Y to confirm: ")
            if confirm == 'Y' or confirm == 'y':
                data.remove(key)
                print(f"{name} category is deleted successfully")
            else:
                print("Not Deleted.")
            break
    else:
        print("Category not found, Please try again!")


def update_expense(data):
    k=1
    for key in data:
        print(f'{k}: {key["category"]}')
        k += 1
    name = input("Please input the category to update: ")
    for key in data:
        if key['category'] == name.capitalize():
            while True:
                try:
                    date = get_date_input()
                    date_timestamp = time.mktime(date.timetuple())

                    # category = input("Please input the Category (e.g., Food, Transportation, Entertainment): ")
                    amount = int(input("Please input the Amount: "))
                    description = input("Please write a brief Description: ")
                    if amount < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Amount should be a positive number")
                    print("Please Try Again")
                    print()
            key['date'] = date_timestamp
            key['amount'] = amount
            key['description'] = description
            break

def readfile(file):
    import os
    data = []

    if not os.path.exists(file):
        return data

    with open(file, 'r') as f:
        for line in f:
            date, amount, category, description = line.strip().split(',')
            lines = {
                'date': date,
                'amount': int(amount),
                'category': category,
                'description': description
            }
            data.append(lines)

    return data

def save_expenses(data, file):
    with open(file, 'w') as myfile:
        for categories in data:
            myfile.write(f"{categories['date']},{categories['amount']},{categories['category']},{categories['description']}\n")

from datetime import datetime

def get_date_input():
    while True:
        date_string = input("Enter a date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_string, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():

    file = "abc.csv"
    data = readfile(file)


    while True:
        print("-----------Expense Tracker------------")
        print("      1 - to Add Expense ")
        print("      2 - to View Expense ")
        print("      3 - to Delete Expense")
        print("      4 - to Edit/Update Expense")
        print("      5 - to Save the Expenses")
        print(" Enter anything to Exit the Program")
        print("---------------------------------------")

        num = input("Enter any choice from 1-5: ")
        if num == '1':
            add_expense(data)
        elif num == '2':
            view_expense(data)
        elif num == '3':
            delete_expense(data)
        elif num == '4':
            update_expense(data)
        elif num == '5':
            save_expenses(data,file)
            print("\nSuccessfully Saved in the Memory\n")

        else:
            print("\nThank you for using Expense Tracker")
            break
main()