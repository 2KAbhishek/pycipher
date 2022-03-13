import unittest
import sys
sys.path.append(".")
from src.vigenere import vigenere

class VigenereTest(unittest.TestCase):
    def test_encrypt_uppercase(self):
        self.assertEqual(vigenere("WE", "CO"), "YS")

    def test_decrypt_uppercase(self):
        self.assertEqual(vigenere("YS", "CO", False), "WE")
