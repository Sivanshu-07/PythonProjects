# password strength checker

import re

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
    
def password_checker():
    """
    Main function to take user input and check password strength.
    """
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")

        if password.lower()=="exit":
            print("Thank you for using the Password Strength Checker! Goodbye!")
            break

        result = check_password_strength(password)
        print(result)

# Run the password checker
if __name__ == "__main__":
    password_checker()

# The upper sentence is used when we want to run specific function and not want to run python code line by line
# and also if code is written somewhere else then it helps to import and run that particular section of code first
