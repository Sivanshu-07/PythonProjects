import json

try:
    with open("PersonalData.json", "r") as file:
        data = json.load(file) # data is a python dictionary
except FileNotFoundError:
    data = {"PersonalData": []} 

def report(expenses):

    if not expenses:
        print("No expenses found.")
        return

    # Total
    total = 0
    for item in expenses:
        total += item["Amount"]

    print("Total Expense :", total)
    print("Average Expense :", total / len(expenses))

    # Category Wise
    print("\nCategory Wise Expenditure:")
    cat_exp = {}

    for item in expenses:
        category = item["Category"]
        amount = item["Amount"]

        if category in cat_exp:
            cat_exp[category] += amount
        else:
            cat_exp[category] = amount

    for key, value in cat_exp.items():
        print(f"{key} : {value}")

    # Highest Expense
    high = expenses[0]["Amount"]
    high_title = expenses[0]["Title"]

    for item in expenses:
        if item["Amount"] > high:
            high = item["Amount"]
            high_title = item["Title"]

    print("\nHighest Expense :", high_title, "of", high)

def save_and_exit(expenses):
    data = {"PersonalData": expenses} # file me likhne se pehle hume wapas wahi structure banana padega.
    with open("PersonalData.json", "w") as file: # yaha jo naam likhenge file ka(.json lagakr) usme hi data save hoga 
        json.dump(data, file, indent=4)  # isme data wo h jo file me jane wala h aur file wo h jo iss line ke just upar likha hai indent = 4 bss formatting k liy hai 

while True:
    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Report")
    print("4. Save & Exit")

    ch = int(input("Enter Your Choice: "))

    match ch:

        case 1:
            title = input("Enter the Title: ")
            amount = int(input("Enter the Amount: "))
            category = input("Enter the Category: ")
            date = input("Enter the Date (YYYY-MM-DD): ")

            expense = {
                "Title": title,
                "Amount": amount,
                "Category": category,
                "Date": date
            }

            data["PersonalData"].append(expense)
            print("Expense Added Successfully!")

        case 2:
            expenses = data["PersonalData"]

            if not expenses:
                print("No expenses found.")
            else:
                print("\nYour Expenses:")
                for exp in expenses:
                    print(f'{exp["Title"]} : {exp["Amount"]}')

        case 3:
            print("\n------ REPORT ------")
            report(data["PersonalData"])

        case 4:
            save_and_exit(data["PersonalData"])
            print("Data Saved Successfully. Exiting...")
            break

        case _:
            print("Invalid Choice! Try Again.")
