#!/usr/bin/env python


import email
from stat import UF_NODUMP
from types import new_class

from sqlalchemy import true
from password import Credentials, User
# user def starts here

def new_user_login(f_name, l_name,u_name, email,password):
    '''new user login'''
    new_user = User(f_name,l_name,u_name,email,password)
    return new_user

def save_user(user):
    '''save user'''
    user.save_user()
    
def check_user(email):
    '''check user'''
    new_user1 = User.user_list(email)
    return new_user1

def user_login(email, password):
    '''user login'''
    the_user = User(email, password)
    return "login success"

def show_user(self):
    '''show user details'''
    return self.user_list

def find_email(email):
    return User.find_by_email(email)



# credential defs  start here


def store_credentials(self):
    '''stores credentials'''
    credential1 = Credentials.Credentials_list.append(self)
    return credential1
 
def remove_credentials(self):
    '''removes credentials'''
    credentials2 = Credentials.Credentials_list.remove(self)
    return credentials2 

def find_credential(account):
    '''finds credentials''' 
    Credentials3 = Credentials.Credentials_list(account)
    return Credentials3

def show_credential (cls):
    '''show credential'''
    return cls.Credentials.Credentials_list


def main():
    print("welcome, To PassWordLOcker enter password to continue")
    
    '''login logic'''
    
    # password = input()
    # if password == True:
    #   return print ("enter User name to continue")
    # else: 
    #     print ("wrong password")
        
    # user_name = input()
    # if user_name == True:
    #     return print(f"welcome {user_name}, lets continue")
    # else:
    #     print ("wrong user")
    
    
    # '''Creation of new account'''
    # print(f"welcome {user_name}, lets continue")
    # print('\n')
    # print("use this short codes for navigation: \n cu-createuser, \n lgn - login if already have account, \n ex-exit on the appliction")
    # short_code = input().lower()
    # if short_code == 'cu':
    #         print("No account no problem,lets make one ")
            
    #         print("New User")
    #         print("First Name")
    #         f_name = input()
            
    #         print("Last Name")
    #         l_name = input()
            
    #         print("User Name")
    #         u_name = input()
            
            
    #         email = input("enter email")
            
    #         print ("password")
    #         password = input()
            
    #         save_user(create_user(f_name,l_name,u_name,email,password))
    #         print('\n')
    #         print(f'Account {f_name}{l_name}{u_name}{email}{password} now exists')
    # elif short_code == 'lgn':
        
    #         print('Enter username:')
    #         u_name = input()
            
            
    #         print('Enter password:')
    #         password = input()
    # while True:
       
    #     print('\n')
    #     print('use short codes to navigate: \n ca -createAccount, \n dc - display_credentials , \n sc - show_specifc_credential, \n D - delete')
       
        
        
          
        
    #     if short_code == 'ca':
    #         print('enter account, eg instagram')
            
    #         print("Account")
    #         account = input()
    #     else:
    #         print("Else statement running")
    #     break
             
            
        # elif short_code == 'ex':
        #     print("come back soon dont be a stranger")
        #     break 
        # else:
        #     print("Invalid, Please use shortcodes") 
             
    '''interacting with credentials'''
    # while True:
       
        # elif short_code == 'dc':
            
                
            
            
    
           
    
        # break    
        
        
           
            
            
             
            
if __name__ == '__main__':
    main()