
# import email
import unittest

import pyperclip
from password import Credentials, User
from password_run import save_user 


# this will be our test site

''' writing tests '''

class TestUser(unittest.TestCase):
    
    '''test for new user'''
    
    def setUp(self):
        self.new_user = User("John","Doe","John Doe","pseudo@gmail.com","123john")
        # self.user1 = User("John Doe", "pseudo@gmail.com", "123john")
        
    def test_init(self):
        self.assertEqual(self.new_user.f_name,"John")
        self.assertEqual(self.new_user.l_name,"Doe")
        self.assertEqual(self.new_user.u_name,"John Doe")
        self.assertEqual(self.new_user.email,"pseudo@gmail.com")
        self.assertEqual(self.new_user.password,"123john")
        
    '''test for user display'''
    
    def tearDown(self):
        ''' test for adding user '''
        User.user_list =[]
    
    def test_save(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_users(self):
        ''' test for adding multiple users '''
        self.new_user.save_user()
        extra_user = User ("John", "Doe", "JohnDoe", "seudo@gmail.com", "123john")   
        extra_user.save_user()
        
        self.assertEqual(len(User.user_list),2)
        
        
    def test_user_exists(self):
        self.new_user.save_user()
        new_user = User("John", "Doe", "JohnDoe", "pseudo@gmail.com", "123john") 
        new_user.save_user()
        email_exists = User.check_user("pseudo@gmail.com")
        self.assertTrue(email_exists)
        
    def test_user_login(self):
        user1 = self.new_user.save_user()
        user1_is_logged = User.user_login("pseudo@gmail.com","123john")
  
        self.assertTrue(user1_is_logged)
        
    def test_new_user_login(self):
        newuser = self.new_user.save_user()
        newuser_has_new_account = User.new_user_login("John","Doe","John Doe","pseudo@gmail.com","123john")
        
        self.assertTrue(newuser_has_new_account)  
        
    def test_check_user(self):
        existing_user = self.new_user.save_user()
        existing_user_has_account = Credentials.check_user("John Doe","123john")
        
        self.assertTrue(existing_user_has_account)        

            
        
    # def test_copy_email(self):
    #     self.new_user.save_user()
    #     User.lookthrough_email("pseudo@gmail.com")
    #     # User.find_by_email("pseudo@gmail.com")
    #     self.assertEqual(self.new_user.email, pyperclip.paste)    
        
 
        
        
if __name__== '__main__':
    unittest.main()
