import unittest
import sys
sys.path.append(".")
from src.caesar import encrypt, decrypt

class CaesarTest(unittest.TestCase):
    def test_encrypt_uppercase_positive_key(self):
        self.assertEqual(encrypt("ABC", 3), "DEF")


