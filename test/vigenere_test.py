import unittest
import sys
sys.path.append(".")
from src.vigenere import encrypt

class VigenereTest(unittest.TestCase):
    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt("WE", "CO"), "YS")
