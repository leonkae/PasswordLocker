
import string


class User:
    '''lets save user data'''
    
    
    user_list = []
    
    def __init__ (self, f_name, l_name, user_name, email,password):
        
        self.f_name = f_name
        self.l_name = l_name
        self.user_name = user_name
        self.email = email
        self.password = password
        
        ''' creating user account'''
        
    def new_user_account (self):
        User.user_list.append(self)
        
    @classmethod
    def user_name_exists(cls,user_name):
        for user in cls.user_list:
            if user_name == {string}:
                return True
            return print("does not accept numbers/special characters")
      
      
        
     

    

