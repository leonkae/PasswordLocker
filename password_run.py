#!/usr/bin/env python

import email
from password import User


def create_user(f_name, l_name,u_name, email):
    new_user = User(f_name,l_name,email)
    return new_user

def save_user(user):
    user.save_user()
    
def find_email(email):
    return User.find_by_email(email)

def main():
    print("welcome, To PassWordLOcker enter password to continue")
    
    '''login logic'''
    
    password = input()
    if password == True:
      return print ("enter User name to continue")
    else: 
        print ("wrong password")
    user_name = input()
    if user_name == True:
        return print(f"welcome {user_name}, lets continue")
    else:
        print ("wrong user")
    
    
    '''Creation of new account'''
    # print(f"welcome {user_name}, lets continue")
    print('\n')
    while True:
        print("This short codes: cu-createuser, fm-findmail, ex-exit on the appliction")
        short_code = input().lower()
        if short_code == 'cu':
            print("No account no problem")
            
            print("New User")
            print("First Name")
            f_name = input()
            
            print("Last Name")
            l_name = input()
            
            print("User Name")
            u_name = input()
            
            print ("Email")
            email = input()
            
            print ("password")
            password = input()
            
            save_user(create_user(f_name,l_name,u_name,email,password))
            print('\n')
            print(f'Account {f_name}{l_name}{u_name}{email}{password} now exists')
            
            
        elif short_code == 'ex':
            print("come back soon dont be a stranger")
            break 
        else:
            print("Invalid, Please use shortcodes")  
            
             
            
if __name__ == '__main__':
    main()