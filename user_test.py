
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

        
        
        
if __name__== '__main__':
    unittest.main()
