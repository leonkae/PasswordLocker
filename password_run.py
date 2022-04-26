#!/usr/bin/env python

from unicodedata import name
from password import Credentials, User
# user def starts here

def new_user_login(f_name, l_name,u_name, email,password):
    '''new user login'''
    new_user = User(f_name,l_name,u_name,email,password)
    return new_user

def save_user(user):
    '''save user'''
    return user.save_user()
    
def check_user(email):
    '''check user'''
    new_user1 = User.user_list(email)
    return new_user1

def user_login(email, password):
    '''user login'''
    # the_user = User(email, password)
    user=  User.user_login(email, password)
    if not user:
        username, password = ask_for_login_details()
        return user_login(username, password)
    return user
    # return print("login success")

def show_user(self):
    '''show user details'''
    return self.user_list

def find_email(email):
    return User.find_by_email(email)

def ask_for_login_details():
    email = input("Enter email: ")
    password = input("Enter password: ")
    return [email, password]


 


def store_credentials(account, u_name, password):
    '''stores credentials'''
    # credential1 = Credentials.Credentials_list.append(self)
    new_acount = Credentials(account,u_name,password)
    account = new_acount.store_credentials()
    if account:
        print("Account created successfully!\n")
        return account
    
 
def remove_credentials(user,account):
    '''removes credentials'''
    credentials = show_me_accounts()
    for c in credentials:
        if c.account == account:
           print(f"{c.account} deleted successfully")
           return credentials.remove(c)
    

def find_credential(account):
    '''finds credentials''' 
    Credentials3 = Credentials.Credentials_list(account)
    return Credentials3

def show_credential (user):
    '''show credential'''
    credentials =  user.show_credential()
    return credentials
    


def show_me_accounts ():
    credentials = Credentials.show_credentials()
    for credential in credentials:
        print(credential.account)
        print(credential.u_name)
        print(credential.password)
    return credentials


    


def main():
    print("welcome, To PassWordLOcker enter password to continue")
    print("To exit use: ex")
    
    '''login logic'''
       
    user = None
    
    
    
    print("Please create an account")
    f_name = input("Enter your first name>>: ")
    l_name = input("Enter your last name>>: ")
    # print("User Name")
    u_name = f_name + l_name
    print("Your username is: ", u_name)


    email = input("enter email>>: ")

    password = input("Enter password>>: ")

    account_created = save_user(new_user_login(f_name,l_name,u_name,email,password))
    if account_created:
        
        print(f'\nAccount created successfully!')
        email, password = ask_for_login_details()
        # Login user with above username and password
        new_user = user_login(email, password)
        if new_user:
         user = new_user
            
            
        
   
            
    while True:
        
              
        if user:
            print('\nuse short codes to navigate: \n ca -createAccount, \n dc - display_credentials , \n D - delete\n')
                
            short_code = input("Select an action using the above shortcode: ")
           
          
        
            if short_code == 'ca':
                
                account = input("\nEnter account name, eg Instagram: ")
                u_name = input( "enter account user name:")
                password = input ("enter accont email>>:")
                account = store_credentials(account, u_name, password)
          
            elif short_code == 'dc':
                print("DC")
                # show_credential = Credentials(u_name, password)
                show_me_accounts()
                
            elif short_code == "D":
                print("Delete")
                account = input("Enter account to delete: ")
                print("Account to delete>>: ", account)
                remove_credentials(user, account)
                
            elif short_code == 'ex':
                print("Exit")
            else: 
                print("Please select from above shortcode")
        
             
 
            
if __name__ == '__main__':
    main()