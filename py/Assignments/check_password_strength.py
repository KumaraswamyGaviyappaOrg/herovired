#Functionm to check password strength

#!/bin/python3
def check_password_strength(password):
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char in "!@#$%^&*()-+" for char in password):
        return False
    else:
        return True
    
if __name__ == '__main__':
    
    while True:
        if(check_password_strength(password = input(" ○ The password should be at least 8 characters long.\n ○ Contains both uppercase and lowercase letters.\n ○ Contains at least one digit (0-9).\n ○ Contains at least one special character (e.g., !, @, #, $, %).\n Enter the password: "))): 
            print("Strong Password") 
            break
        else: 
            print("Weak Password")