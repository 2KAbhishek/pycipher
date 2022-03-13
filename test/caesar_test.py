import unittest
import sys
sys.path.append(".")
from src.caesar import caesar

class CaesarTest(unittest.TestCase):
    def test_encrypt_uppercase_positive_key(self):
        self.assertEqual(caesar("ABC", 3), "DEF")

    def test_decrypt_uppercase_positive_key(self):
        self.assertEqual(caesar("DEF", 3, False), "ABC")

    def test_encrypt_with_whitespace(self):
        self.assertEqual(caesar("A B C", 3), "D E F")


