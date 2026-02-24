<<<<<<< HEAD
# password strength checker

import re
import FreeSimpleGUI as sg

# password strength check conditions:
# min 8 chars, digit, uppercase,lowercase, special char

def check_password_strength(password):
    
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(){}|.,<>]',password):
        return "Medium: Add special characters to make your password stronger."
    
    return "Strong: Your Password is secure!"

# Ui layout

layout = [
    [sg.Text("Password Strength Checker",font=("Ariel",16))],

    [sg.Text("Enter Password:"),
     sg.Input(key="PWD",password_char="*")],

    [sg.Button("Check Strength"),sg.Button("Exit")],

    [sg.Text("Result:",font=("Ariel",12,"bold"))],

    [sg.Text("",size = (50,2),key="RESULT")]    
]

#create Window

window = sg.Window("Password Checker App",layout)

# Event Loop

while True:
    event,values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Check Strength":

        password = values["PWD"]

        if password == "":
            window["RESULT"].update("Please enter a password first!")
        else :
            result = check_password_strength(password)
            window["RESULT"].update(result)
    print(window)

=======
# password strength checker

import re
import FreeSimpleGUI as sg

# password strength check conditions:
# min 8 chars, digit, uppercase,lowercase, special char

def check_password_strength(password):
    
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(){}|.,<>]',password):
        return "Medium: Add special characters to make your password stronger."
    
    return "Strong: Your Password is secure!"

# Ui layout

layout = [
    [sg.Text("Password Strength Checker",font=("Ariel",16))],

    [sg.Text("Enter Password:"),
     sg.Input(key="PWD",password_char="*")],

    [sg.Button("Check Strength"),sg.Button("Exit")],

    [sg.Text("Result:",font=("Ariel",12,"bold"))],

    [sg.Text("",size = (50,2),key="RESULT")]    
]

#create Window

window = sg.Window("Password Checker App",layout)

# Event Loop

while True:
    event,values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Check Strength":

        password = values["PWD"]

        if password == "":
            window["RESULT"].update("Please enter a password first!")
        else :
            result = check_password_strength(password)
            window["RESULT"].update(result)
    print(window)

>>>>>>> e0d4995 (Added Personal Expense Tracker Project)
window.close()    