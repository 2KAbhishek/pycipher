import unittest
import sys
sys.path.append(".")
from src.vigenere import encrypt, decrypt

class VigenereTest(unittest.TestCase):
    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt("WE", "CO"), "YS")

    def test_decrypt_uppercase(self):
        self.assertEqual(decrypt("YS", "CO"), "WE")
