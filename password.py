import pyperclip
import string


class User:
    '''lets save user data'''
    
    
    user_list = []
    
    def __init__ (self, f_name, l_name, u_name, email,password):
        
        self.f_name = f_name
        self.l_name = l_name
        self.user_name = u_name
        self.email = email
        self.password = password
        
        ''' creating user account'''
        
    def save_user (self):
        User.user_list.append(self)
        
        '''method that checks for string data type'''
    @classmethod
    def f_name_exists(cls,f_name):
        for user in cls.user_list:
            if user.f_name == {string}:
                return True
            return print ("does not accept numbers/special character")    
        
        
        '''method that checks for string data type'''
    
    @classmethod
    def l_name_exists(cls,l_name):
        for user in cls.user_list:
            if user.l_name == {string}:
                return True
            return print ("does not accept numbers/special character")
              
        '''method that checks for string data type'''
        
    @classmethod
    def user_name_exists(cls,u_name):
        for user in cls.user_list:
            if user.u_name == {string}:
                return True
            return print("does not accept numbers/special characters")
       
       
        '''email check'''

    @classmethod
    def copy_email(cls,email):
        email_found = User.find_by_email(email)
        pyperclip.copy(email_found)
        
        
        '''password logic'''
    @classmethod
    def enter_password(cls,password):
        password   
     
      
      
