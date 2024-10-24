import time
import random
from unicodedata import category


def add_expense(data):
    date = get_date()
    date_timestamp = date.timestamp()
    category = get_category()
    amount = get_amount()
    description = input("Please write a brief Description: ")
    myid = random.randint(0,100)
    new_expense = {
        'category': category,
        'amount': amount,
        'date': date_timestamp,
        'description': description,
        'id': myid
    }
    if isinstance(data, list):
        data.append(new_expense)
    else:
        data = [new_expense]
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
        print('Id          Date          Expenses             Category                Description')
        for key in data:
            total += int(key['amount'])
            print(f"{key['id']:<12}{key['date']:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")
        print('-' *72)
        print(f"\nYour Overall Expense is: {total} \n")
    elif choice == '2':
        k = 1
        for key in data:
            print(f'{k}: {key["category"]}')
            k += 1
        cat = input("If you want to calculate expense by category then enter category name: ")
        cat_total = 0
        print('Id          Date          Expenses             Category                Description')
        for key in data:
            if key['category'] == cat.capitalize():
                print(f"{key['id']:<12}{key['date']:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")
                cat_total += key['amount']

        print(f'Overall Expense of {cat} Category is {cat_total}')
    elif choice == '3':
        print("If you want to calculate expense by Date then enter Date : ")
        date = get_date()
        date = date.timestamp()

        print('id          Category          Expenses         Description ')
        for key in data:
            if key['date'] == date:
                print(f"{key['id']:<12} {key['category']:<15}  {key['amount']:<15} {key['description']:<15}")

    else:
        print(" Invalid Choice")

def monthly_expense(data):
    import calendar
    from datetime import datetime

    if not data:
        print("Data not found")
        return

    month = get_month()
    year = int(month.strftime("%Y"))
    months = int(month.strftime("%m"))
    month_name = month.strftime("%B")

    first = datetime(year,months,1)
    last = calendar.monthrange(year,months)[1]
    last = datetime(year,months,last)
    total = 0

    print('Id          Date          Expenses             Category                Description')
    for key in data:
        if first.timestamp() <= float(key['date']) <= last.timestamp():
            total += float(key['amount'])
            print(f"{key['id']:<12}{key['date']:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")

    print(f"\nOverall Expenses for {month_name}-{year} is {total} \n")

def delete_expense(data):
    print('Id          Date          Expenses             Category                Description')
    for key in data:
        print(f"{key['id']:<12}{key['date']:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")

    id = int(input("\nPlease Select an id which you want to delete: "))

    for key in data:
        if key['id'] == id:
            confirm = input("Press Y to confirm: ")
            if confirm == 'Y' or confirm == 'y':
                data.remove(key)
                print(f"{id} id is deleted successfully")
            else:
                print("Not Deleted.")
            break
    else:
        print("Id not found, Please try again!")


def update_expense(data):
    print('Id          Date          Expenses             Category                Description')
    for key in data:
        print(f"{key['id']:<12}{key['date']:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")

    id = int(input("Please input the category to update: "))
    for key in data:
        if key['id'] == id:
            while True:
                try:
                    date = get_date()
                    date_timestamp = date.timestamp()
                    category = get_category()
                    amount = get_amount()
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
            key['category'] = category
            key['description'] = description
            break

def readfile(file):
    import os
    data = []

    if not os.path.exists(file):
        return data

    with open(file, 'r') as f:
        for line in f:
            id, date, amount, category, description = line.strip().split(',')
            lines = {
                'id':int(id),
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
            myfile.write(f"{categories['id']},{categories['date']},{categories['amount']},{categories['category']},{categories['description']}\n")

from datetime import datetime

def get_date():
    while True:
        date_string = input("Enter a date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_string, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_category():
    while True:
        try:
            category_list = ['Food', 'Transportation', 'Entertainment', 'Sports', 'Home', 'Others']
            category = input(
                "Enter Category (e.g., Food, Transportation, Entertainment, Sports, Home, Others): ").capitalize()
            if category not in category_list:
                raise ValueError
            return category
        except ValueError:
            print("Category not found in the Mentioned list, Please try again")


def get_amount():
    while True:
        try:
            amount = int(input("Please input the amount: "))
            if amount<0:
                raise ValueError
            return amount
        except ValueError:
            print("Amount should a positive number and greater than zero")

def get_month():
    while True:
        month = input("Enter a Year and Month (YYYY-MM): ")
        try:
            month = datetime.strptime(month, "%Y-%m")
            return month
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
        print("      5 - to get monthly report")
        print("      6 - to Save the Expenses")
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
            monthly_expense(data)
        elif num == '6':
            save_expenses(data,file)
            print("\nSuccessfully Saved in the Memory\n")

        else:
            print("\nThank you for using Expense Tracker")
            break
main()