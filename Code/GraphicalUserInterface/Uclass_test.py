import unittest

from User import User

class UsertClassTest(unittest.TestCase):

    testuser = {
        "name": "testuser",
        "password": "pass1234",
        "email": "user@gmail.com"
    }

    def test_ValidateUser(self):
        self.assertEqual(User.ValidateUser(self.testuser["name"]), True)

    def test_ValidateMail(self):
        self.assertEqual(User.ValidateMail(self.testuser["email"]), True)

    def test_ValidatePassword(self):
        self.assertEqual(User.ValidatePassword(self.testuser["password"]), False)

if __name__=="__main__":
    unittest.main()