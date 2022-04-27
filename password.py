

import string
import random



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
                return user
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
        print("this has user information")
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
        
        
    
    
    def __init__(self,account, u_name, password ):
        
        '''defining credential terms'''
        self.account = account
        self.u_name = u_name
        self.password = password
        # self.email = email
        
        
        
    def store_credentials(self):
        '''adding credetials to credentials_list (save)''' 
        Credentials.Credentials_list.append(self)
        return self
        
        
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
                print ("credential present")
                return True
        print ("credential absent")    
        return False 
    
    
    @classmethod
    def show_credentials(cls):
        '''shows credentials '''
        print("Here are your accounts...")
        print("\n")
        return cls.Credentials_list  
    
    def constructPassword(length=4):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*``~-_=+\|][?"
        return ''.join(random.choice(password) for i in range(length))
    