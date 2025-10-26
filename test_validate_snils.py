import unittest
from validate_snils import *

class TestValidateSnils(unittest.TestCase):
    
    def test_valid_snils_with_correct_checksum(self):
        # Тестирование правильного СНИЛС с корректной контрольной суммой
        self.assertTrue(validate_snils("123-456-789 64"))
    
    def test_valid_snils_with_zero_checksum(self):
        # Тестирование СНИЛС с нулевой контрольной суммой
        self.assertTrue(validate_snils("000-000-000 00"))
        
    def test_invalid_snils_format(self):
        # Тестирование неправильного формата СНИЛС
        self.assertFalse(validate_snils("12345678901"))
        self.assertFalse(validate_snils("12-34-56 78"))
        self.assertFalse(validate_snils("abc-def-ghi kl"))
        
    def test_invalid_snils_length(self):
        # Тестирование СНИЛС с неправильной длиной
        self.assertFalse(validate_snils("123-456-78 90"))
        self.assertFalse(validate_snils("123-456-789 012"))
        
    def test_invalid_snils_checksum(self):
        # Тестирование СНИЛС с неправильной контрольной суммой
        self.assertFalse(validate_snils("123-456-789 99"))
        
    def test_ok(self):
        self.assertTrue(validate_snils("161-394-864 82"))
    def test_ok_file(self):
        self.assertTrue(validate_snils_from_file("sample_snils.txt"))
    def test_invalid_file(self):
        self.assertFalse(validate_snils_from_file("invalid_file.txt"))
    def test_from_url(self):
        self.assertTrue(validate_snils_from_url("https://www.consultant.ru/document/cons_doc_LAW_167281/c2bc8375b3c705a61bdd1f284d9db2070929c0a7/"))
    def test_invalid_from_urk(self):
        self.assertFalse(validate_snils_from_url("https://edu.stankin.ru/course/view.php?id=11060"))