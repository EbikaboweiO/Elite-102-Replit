import unittest
from website.auth import *

class PasswordsMatchTestCase(unittest.TestCase):
    def test_passwords_match(self, password):
        self.assertTrue(check_password_hash('pbkdf2:sha256:150000$C2kZo8q0$1f2e1d8c7b6a59e8', password))
