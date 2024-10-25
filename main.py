import random

def add_expense(data):
    date = get_date()
    date_timestamp = date.timestamp()
    category = get_category()
    amount = get_amount()
    description = input("Please write a brief Description: ")
    id1 = random.randint(0,500)
    new_expense = {
        'category': category,
        'amount': amount,
        'date': date_timestamp,
        'description': description,
        'id': id1
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
            date = key['date']
            date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
            total += int(key['amount'])
            print(f"{key['id']:<12}{date:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")
        print('-' *72)
        print(f"\nYour Overall Expense is: {total} \n")

    elif choice == '2':
        print('Id          Date          Expenses             Category                Description')
        for key in data:
            date = key['date']
            readable_date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
            print(f"{key['id']:<12}{readable_date:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")
        cat = input("\nIf you want to filter expense by category then enter category name: ")
        cat_total = 0
        print('Id          Date          Expenses             Category                Description')
        for key in data:
            if key['category'] == cat.capitalize():
                print(f"{key['id']:<12}{key['date']:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")
                cat_total += key['amount']
        print(f'Overall Expense of {cat} Category is {cat_total}')

    elif choice == '3':
        print("If you want to filter expense by Date then enter Date : ")
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
            date = key['date']
            date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
            total += float(key['amount'])
            print(f"{key['id']:<12}{date:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")

    print(f"\nOverall Expenses for {month_name}-{year} is {total} \n")

def delete_expense(data):
    print('Id          Date          Expenses             Category                Description')
    for key in data:
        date = key['date']
        date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
        print(f"{key['id']:<12}{date:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")

    # id1 = int(input("\nPlease Select an id which you want to delete: "))
    #
    # for key in data:
    #     while True:
    #         try:
    #             if key['id'] == id1:
    #                 confirm = input("Press Y to confirm: ")
    #                 if confirm == 'Y' or confirm == 'y':
    #                     data.remove(key)
    #                     print(f"{id1} id is deleted successfully")
    #                 else:
    #                     print("Not Deleted.")
    #             else:
    #                 raise ValueError
    #
    #         except ValueError:
    #             print(f"{id1} not found please try again")
    #             break
    try:
        id1 = int(input("\nPlease select an id you want to delete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
    else:
        id_found = False

        for key in data:
            if key['id'] == id1:
                confirm = input("Press Y to confirm: ").strip()
                if confirm in ('Y', 'y'):
                    data.remove(key)
                    print(f"{id1} id is deleted successfully")
                else:
                    print("Not Deleted.")
                id_found = True
                break  # Exit the loop after deletion

        # If the id wasn't found, provide feedback
        if not id_found:
            print(f"{id1} not found, please try again.")


def update_expense(data):
    print('Id          Date          Expenses             Category                Description')
    for key in data:
        date = key['date']
        date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
        print(f"{key['id']:<12}{date:<15} {key['amount']}     {key['category']:>15}  {key['description']:>27}")

    # id1 = int(input("Please input the id to update: "))
    try:
        id1 = int(input("\nPlease select an id you want to Update: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
    else:
        for key in data:
            if key['id'] == id1:

                date = get_date()
                date_timestamp = date.timestamp()
                category = get_category()
                amount = get_amount()
                description = input("Please write a brief Description: ")

                key['date'] = date_timestamp
                key['amount'] = amount
                key['category'] = category
                key['description'] = description

def readfile(file):
    import os
    data = []

    if not os.path.exists(file):
        return data

    with open(file, 'r') as f:
        for line in f:
            id1, date, amount, category, description = line.strip().split(',')
            lines = {
                'id':int(id1),
                'date': float(date),
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