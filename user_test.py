
# import email
from tabnanny import check
import unittest
from django.forms import SelectDateWidget

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
        '''tests addition of 1 user'''
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
        '''tests login logic'''
        user1 = self.new_user.save_user()
        user1_is_logged = User.user_login("pseudo@gmail.com","123john")
  
        self.assertTrue(user1_is_logged)
        
    def test_new_user_login(self):
        newuser = self.new_user.save_user()
        newuser_has_new_account = User.new_user_login("John","Doe","John Doe","pseudo@gmail.com","123john")
        
        self.assertTrue(newuser_has_new_account) 
        
    def test_show_user(self):
        self.assertEqual(User.show_user(),User.user_list)     
        
class Testcredentials(unittest.TestCase) :
    
    '''tests for credentials'''
    
    def setUp(self):
        self.new_credential = Credentials("john Doe" , "pseudo@gmail.com", "123John", "instagram")
        
    def test_init(self):
         '''testing for credential initialising'''
         self.assertEqual(self.new_credential.u_name,'john Doe')
         self.assertEqual(self.new_credential.email,'pseudo@gmail.com')
         self.assertEqual(self.new_credential.password, '123John')
         self.assertEqual(self.new_credential.account,'instagram')
              
    
    def test_store_credentials(self): 
        '''tests for credential storage'''
        self.new_credential.store_credentials()
        self.assertEqual(len(Credentials.Credentials_list),6)

        
         
    def test_remove_credentials(self):
        '''tests for credential removal'''
        self.new_credential.store_credentials()
        self.assertEqual(len(Credentials.Credentials_list),5) 
        
        
    def test_find_credential(self):
        '''testing (find credential) method'''
        self.new_credential.store_credentials()
        credential_check = Credentials("john Doe" , "pseudo@gmail.com", "123John", "instagram")
        credential_check.store_credentials()
        
        cred = Credentials.find_credential("instagram")
        
        self.assertEqual(credential_check.account,cred.account)
        
    def test_credential_present(self):
        self.new_credential.store_credentials()
        account_credential = Credentials("john Doe" , "pseudo@gmail.com", "123John", "instagram")
        account_credential.store_credentials()
        
        credential_exists = Credentials.credential_present("instagram")
        
        self.assertTrue(credential_exists)
        
    def test_show_credentials(self):
        self.assertEqual(Credentials.show_credentials(),Credentials.Credentials_list)
        
        
    # def test_copy_email(self):
    #     self.new_user.save_user()
    #     User.lookthrough_email("pseudo@gmail.com")
    #     # User.find_by_email("pseudo@gmail.com")
    #     self.assertEqual(self.new_user.email, pyperclip.paste)    
        
 
        
        
if __name__== '__main__':
    unittest.main()
