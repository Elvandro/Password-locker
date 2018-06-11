import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("Elvis","elvisamuni22@gmail.com","Elvizy254")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Elvis")
        self.assertEqual(self.new_user.email,"elvisamuni22@gmail.com")
        self.assertEqual(self.new_user.password,"Elvizy254")

    def test_save_user(self):
        '''
        test_save_user method to save a user
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
