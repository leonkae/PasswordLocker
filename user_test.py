
import email
import unittest

import pyperclip
from password import User 


# this will be our test site

''' writing tests '''

class TestUser(unittest.TestCase):
    
    '''test for new user'''
    
    def setUp(self):
        self.new_user = User("John","Doe","John Doe","pseudo@gmail.com","")
        
    def test_init(self):
        self.assertEqual(self.new_user.f_name,"John")
        self.assertEqual(self.new_user.l_name,"Doe")
        self.assertEqual(self.new_user.u_name,"John Doe")
        self.assertEqual(self.new_user.email,"pseudo@gmail.com")
        self.assertEqual(self.new_user.password,"")
        
    '''test for user display'''
    
    def tearDown(self):
        User.user_list =[]
    
    def test_save(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_users(self):
        self.new_user.save_user()
        extra_user = User ("John", "Doe", "JohnDoe", "pseudo@gmail.com", "")   
        extra_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
    def test_email_exists(self):
        self.new_user.save_user()
        new_user = ("John", "Doe", "JohnDoe", "pseudo@gmail.com", "") 
        new_user.save_user()
        email_exists = User.email_exists("pseudo@gmail.com")
        self.assertTrue(email_exists)
        
        
    def test_copy_email(self):
        self.new_user.save_user()
        User.copy_email("pseudo@gmail.com")
        self.assertEqual(self.new_user.email, pyperclip.paste)    
        

        
        
if __name__== '__main__':
    unittest.main()
