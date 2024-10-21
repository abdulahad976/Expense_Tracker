import time
from unicodedata import category


def add_expense(data):
    while True:
        category_list = ['Food','Transportation','Entertainment','Sports', 'Home', 'Others']
        try:
            date = get_date_input()
            # print(type(date))
            unixdate= time.mktime(date.timetuple())
            category = input("Enter Category (e.g., Food, Transportation, Entertainment, Sports, Home, Others): ")
            if not category.capitalize() in category_list:
                print("Category not found")
                return False
            amount = int(input("Please input the Amount: "))
            description = input("Please write a brief Description: ")
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Amount should be a positive number")
            print("Please Try Again")

    # if category in data:
    #     data[category].append(amount)
    # else:
    #     data[category] = [amount]

    # data.update({'category': category, 'amount': [amount], 'description': description})
    # print(data)

    print(f"\nExpense added successfully: Spent {amount} on {category} by {date}\n")
    if unixdate in data:
        data['amount'] += amount
        data['date'] = unixdate
        data['description'] = description
    else:
        data[unixdate] = {'category': category, 'amount': amount, 'date': unixdate, 'description': description}
    print(data)
    # print(f"\nExpense added successfully: Spent {amount} on {category} by {date}\n")


def view_expense(data):
    if not data:
        print("\nNo Data Found \n ")
        return
    total = 0
    sports = 0
    food = 0
    print('Date          Expenses             Category                Description')
    for date, expenses in data.items():
        # if expenses.__getitem__('category') == 'sports':
        #     sports += expenses.__getitem__('amount')
        # if expenses.__getitem__('category') == 'food':
        #     food += expenses.__getitem__('amount')
        # for i,j in expenses.items():
        #     print(i,j)
        total +=  expenses['amount']
        print(f"{date:<15} {expenses['amount']}     {expenses['category']:>15}  {expenses['description']:>27}")
    print('-'*56)
    print(f"\nYour Overall Expense is: {total} \n")
    cat = input("If you want to calculate expense by category then enter category name: ")
    cat_total = 0
    for key, value in data.items():
        if value['category'] == cat:
            cat_total += value['amount']
    print(f'Overall Expense of {cat} Category is {cat_total}')


def delete_expense(data):
    print(data)
    k=1
    for i,j in data.items():
        print(f'{k}: {j["category"]}')
        k +=1
    name = input("\nPlease Select a Category which you want to delete: ")

    for key, value in data.items():
        if value['category'] == name:
            confirm = input("Press Y to confirm: ")
            if confirm == 'Y' or confirm == 'y':
                del data[key]
                print(f"{name} category is deleted successfully")
            else:
                print("Deletion cancelled.")
            break
    else:
        print("Category not found, Please try again!")


def update_expense(data):
    k=1
    for i, j in data.items():
        print(f'{k}: {j["category"]}')
        k += 1
    name = input("Please input the category to update: ")
    for key, value in data.items():
        if value['category'] == name:
            while True:
                try:
                    date = get_date_input()
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

            data[key]['amount'] = amount
            data[key]['description'] = description
            data[key]['date'] = date
            break

def readfile(file):
    import os
    import ast
    data = {}
    if os.path.exists(file):
        with open(file, 'r') as f:
            for line in f:
                date,amount,category,description = line.strip().split(',')
                # data[cat] = ast.literal_eval(amount)
                data[date] = {'amount':int(amount),'category':category,'description':description}
    return data


def save_expenses(data, file):
    with open(file, 'w') as myfile:
        for categories, expenses in data.items():
            myfile.write(f"{categories},{expenses['amount']},{expenses['category']},{expenses['description']}\n")

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