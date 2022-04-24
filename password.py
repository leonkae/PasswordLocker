from multiprocessing.dummy.connection import families
import pyperclip
import string

from sqlalchemy import false


class User:
    '''lets save user data'''
    
    
    user_list = []
    
    def __init__ (self, f_name, l_name, u_name, email,password):
        
        self.f_name = f_name
        self.l_name = l_name
        self.u_name = u_name
        self.email = email
        self.password = password
        
        ''' creating user account'''
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
    
    
    @classmethod    
    def user_login(cls,email,password):
        for user in cls.user_list:
            if user.email == email and user.password == password: 
                print("logged in Succesfully") 
                return True
        print ("wrong email or password, please try again.")
        return False    
            
                
                
            
        # if new_account:
        #     print ("set up account")
        #     return True
        # return False
    
         # @classmethod
         # def check_account (cls, account):
         #     if account:
         #         return True
         #     return False
            
            
        
        

        
        '''method that checks for string data type'''
        
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
     
      
      
