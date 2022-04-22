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
    print("welcome, This to PassWordLOcker")
    user_name = input()
    print(f"welcome {user_name}, lets continue")
    print('\n')
    while True:
        print("This short codes: cu-createuser, fm-findmail, ex-exit on the appliction")
        short_code = input().lower()
        if short_code == 'cu':
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
            
            
if __name__ == '__main__':
    main()