
import unittest
from password import User 


# this will be our test site

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User("John","Doe","John Doe","pseudo@gmail.com","")
        
    def test_init(self):
        self.assertEqual(self.new_user.f_name,"John")
        self.assertEqual(self.new_user.l_name,"Doe")
        self.assertEqual(self.new_user.user_name,"John Doe")
        self.assertEqual(self.new_user.email,"pseudo@gmail.com")
        self.assertEqual(self.new_user.password,"")
    
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
    
        
              

        
        
        
if __name__== '__main__':
    unittest.main()
