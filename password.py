from multiprocessing.dummy.connection import families
from os import uname
from django.urls import translate_url
import pyperclip
import string

from sqlalchemy import false, true


class User:
    '''lets save user data'''
    
    
    user_list = []
    
    def __init__ (self, f_name, l_name, u_name, email,password):
        
        self.f_name = f_name
        self.l_name = l_name
        self.u_name = u_name
        self.email = email
        self.password = password
        
        ''' user account info '''
        
    # @classmethod    
    
    def save_user (self):
        # check_user == user_exists
        has_account = self.check_user(self.email)
        if has_account:
            # print("user exists,not saved")
            return False
        self.user_list.append(self)
        return True
            
       
    @classmethod    
    def check_user(cls,email):
        for user in cls.user_list:
            if user.email == email:
                return True
        return False
    
    ''' login protocal for existing account'''
    @classmethod    
    def user_login(cls,email,password):
        for user in cls.user_list:
            if user.email == email and user.password == password: 
                print("logged in Succesfully") 
                return True
        print ("Wrong email or password, please try again.")
        return False 
    
    ''' new account creation protocal '''
    
    @classmethod
    def new_user_login(cls,f_name,l_name,u_name,email,password):
        for user in cls.user_list:
            if user.f_name == f_name and user.l_name == l_name and user.u_name == u_name and user.email == email and user.password == password:
                print ("User account created Successfully")
                return True 
        print ("Check your details") 
        return False   
    
    @classmethod
    def show_user(self):
        return self.user_list   
            
            
                          
class Credentials():
    ''' credential logic'''
    
    Credentials_list = []
    @classmethod
    def check_user(cls,u_name,password):
        '''checks if user account exists'''
        
        new_user = "",""
        for user in User.user_list:
            if user.u_name == u_name and user.password == password:
                return new_user
        
        
    
    
    def __init__(self,u_name, email, password,account ):
        
        '''defining credential terms'''
        self.u_name = u_name
        self.email = email
        self.password = password
        self.account = account
        
        
        
    def store_credentials(self):
        '''adding credetials to credentials_list (save)''' 
        print("added ++")
        Credentials.Credentials_list.append(self)
        
        
    def remove_credentials(self):
        '''removing credentials from credentials list (delete)'''
        Credentials.Credentials_list.remove(self)     
    
    @classmethod
    def find_credential(cls, account):
        '''this finds, specific accounts'''
        
    
        for credential in cls.Credentials_list:
            if credential.account == account:
                print ("account present")
                return credential
            
            
    @classmethod
    def credential_present(cls, account):
        '''checks if credential is present'''
        
        for credential in cls.Credentials_list:
            if credential.account == account:
                return True
        return False 
    
    
    @classmethod
    def show_credentials(cls):
        '''shows credentials '''
        return cls.Credentials_list           
        
     
            
        # if new_account:
        #     print ("set up account")
        #     return True
        # return False
    
         # @classmethod
         # def check_account (cls, account):
         #     if account:
         #         return True
         #     return False
            
            
        
        

        

        
    # @classmethod
    # def f_name_exists(cls,f_name):
    #     for user in cls.user_list:
    #         if user.f_name == {string}:
    #             return True
    #         return print ("does not accept numbers/special character")    
        
        
        
    #     '''method that checks for string data type'''
    
    # @classmethod
    # def l_name_exists(cls,l_name):
    #     for user in cls.user_list:
    #         if user.l_name == {string}:
    #             return True
    #         return print ("does not accept numbers/special character")
              
    #     '''method that checks for string data type'''
        
    # @classmethod
    # def user_name_exists(cls,u_name):
    #     for user in cls.user_list:
    #         if user.u_name == {string}:
    #             return True
    #         return print("does not accept numbers/special characters")
       
       
    #     '''email check'''

    # @classmethod
    # def lookthrough_email(cls,email):
    #     email_found = User.find_by_email(email)
    #     pyperclip.copy(email_found)
        
    # @classmethod
    # def find_by_email(cls,email):
    #     pass 

        
    #     '''password logic'''
        
    # @classmethod
    # def enter_password(cls,password):
    #     password   
     
      
      
