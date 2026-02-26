import json

try:
    with open("accounts.json",'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"accounts":{}}

def find_account(accNo):
    return data["accounts"].get(accNo) # if account number exist then return its value and if account no. does not exist then it will return None

def create_account():
    while True:
        accNo = (input("Enter the account number : "))
        acc = find_account(accNo)
        if acc:
            print(f'{accNo} already exist !')
            continue
        else:
            break

    name = input("Enter Your Name : ")
    while True: 
        acctype = input("Enter Account Type -> Saving/Current : ")
        if acctype == "saving" or acctype == "current":
            break
        else:
            print("Enter properly !")

    inital_amt = int(input("Enter Initial Amount : "))
    print(f'Account No.{accNo} Created Succesfully ')
    data["accounts"][accNo] = {
            "name":name,
            "account_type":acctype,
            "balance":inital_amt,
            "transactions":[
                {"type":"deposit","amount":inital_amt}
            ]
        }

def deposit():
    while True:
        accNo = input("Enter the Account Number : ")
        acc = find_account(accNo)
        if acc is not None:
            amt = int(input("Enter the amount you want to deposit : "))
            deposit = {"type":"deposit","amount":amt}
            acc["balance"] += amt
            acc["transactions"].append(deposit)
            print(f"{amt} deposited in account no.{accNo} successfully")
            break
        else:
            print("Wrong Account Number ! Please try Again")
            continue
def withdraw():
    while True:
        accNo = input("Enter the Account Number : ")
        acc = find_account(accNo) 
        if acc:
            amt = int(input("Enter the amount to withdraw : "))
            withdw = {"type":"withdraw","amount":amt}
            acc["balance"] -= amt
            acc["transactions"].append(withdw)
            print(f"{amt} withdrawn from account no.{accNo} successfully")
            break
        else:
            print("Wrong Account Number ! Please Try Again")
            continue

def Check_Balance():
    while True:
        accNo = input("Enter the account number : ")
        acc = find_account(accNo)
        if acc:
            print(f"Account Number {accNo} has Balance amount of {acc["balance"]}") 
            break
        else :     
            print("Enter Proper Account Number !")
            continue

def transaction_history():
    while True:
        accNo = input("Enter the account number : ")
        acc = find_account(accNo)
        if acc:
            for items in acc["transactions"]:
                print(f'{items["type"]} : {items["amount"]}')
            return
        else:
            print("Enter Proper Account Number : ")
            continue

def delete_account():
    while True:
        accNo = input("Enter the account number : ")
        acc = find_account(accNo)
        if acc:
            data["accounts"].pop(accNo)
            print(f'Account No.{accNo} deleted Successfully')
            return
        else :
            print("Wrong Account Number ! Please Try Again")
            continue
def Bank_Report():
    highbalance = 0;totalbalance = 0;highbalanceAccNo = 0
    saving_count = 0;current_count = 0
    # accNo_dict = {k:v for k,v in data["accounts"].items()}
    for accNo,accValue in data["accounts"].items():
        if highbalance < accValue["balance"]:
            highbalance = accValue["balance"]
            highbalanceAccNo = accNo
        if accValue["account_type"] == "saving":
            saving_count += 1
        if accValue["account_type"] == "current":
            current_count += 1

        totalbalance += accValue["balance"]
    
    total_account = len(data["accounts"])

    print(f'Total Accounts in the Bank : {total_account}')
    print(f'Total Balance in the Bank : {totalbalance}')
    print(f'Account No.{highbalanceAccNo} has the highest balance {highbalance}')
    print(f'Saving Accounts : {saving_count}')
    print(f'Current Account : {current_count}')
    print("\nAverage Balance : ",totalbalance/total_account)
    

def save_and_exit():
    with open("accounts.json",'w') as file:
        json.dump(data,file,indent = 4 )

while True:
    print("\n\n----Banking System----")
    print("1.Create Account\n2.Deposit\n3.Withdraw\n4.Check Balance\n5.Transaction History\n6.Delete Account\n7.Bank Report\n8.Save & Exit")
    ch = int(input("Enter your choice : "))

    match ch :
        case 1:
            print("\n")
            create_account()
        case 2:
            print("\n")
            deposit()
        case 3:
            print("\n")
            withdraw()
        case 4:
            print("\n")
            Check_Balance()
        case 5:
            print("\n")
            transaction_history()
        case 6:
            print("\n")
            delete_account()
        case 7:
            print("\n----Bank Report----")
            Bank_Report()
        case 8:
            print("\n")
            save_and_exit()
            print("Successfully Saved !")
            break
        case _:
            print("Invalid Choice !")
    
