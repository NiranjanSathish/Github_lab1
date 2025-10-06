"""
Unittest test suite for password_validator.py
"""
import unittest
from src.password_validator import (
    check_length,
    has_uppercase,
    has_lowercase,
    has_digits,
    has_special_chars,
    check_common_patterns,
    calculate_strength_score,
    validate_password
)


class TestPasswordValidator(unittest.TestCase):
    """Test class for password validation functions"""
    
    def test_check_length(self):
        """Test password length validation"""
        self.assertEqual(check_length("12345678"), True)
        self.assertEqual(check_length("1234567"), False)
        self.assertEqual(check_length(""), False)
        self.assertEqual(check_length("VeryLongPassword123!"), True)
    
    def test_has_uppercase(self):
        """Test uppercase letter detection"""
        self.assertEqual(has_uppercase("Password"), True)
        self.assertEqual(has_uppercase("password"), False)
        self.assertEqual(has_uppercase("PASSWORD"), True)
        self.assertEqual(has_uppercase("Pass123!"), True)
    
    def test_has_lowercase(self):
        """Test lowercase letter detection"""
        self.assertEqual(has_lowercase("password"), True)
        self.assertEqual(has_lowercase("PASSWORD"), False)
        self.assertEqual(has_lowercase("Pass123!"), True)
        self.assertEqual(has_lowercase("123456"), False)
    
    def test_has_digits(self):
        """Test digit detection"""
        self.assertEqual(has_digits("Pass123"), True)
        self.assertEqual(has_digits("Password"), False)
        self.assertEqual(has_digits("12345678"), True)
        self.assertEqual(has_digits("Pass!@#"), False)
    
    def test_has_special_chars(self):
        """Test special character detection"""
        self.assertEqual(has_special_chars("Pass@123"), True)
        self.assertEqual(has_special_chars("Password123"), False)
        self.assertEqual(has_special_chars("!@#$%^&*"), True)
        self.assertEqual(has_special_chars("SimplePass"), False)
    
    def test_check_common_patterns(self):
        """Test common pattern detection"""
        self.assertEqual(check_common_patterns("SecurePass!23"), True)
        self.assertEqual(check_common_patterns("password123"), False)
        self.assertEqual(check_common_patterns("qwerty456"), False)
        self.assertEqual(check_common_patterns("MyP@ssw0rd"), True)
    
    def test_calculate_strength_score(self):
        """Test password strength score calculation"""
        self.assertEqual(calculate_strength_score("Pass@123"), 70)
        self.assertEqual(calculate_strength_score("weak"), 25)
        self.assertEqual(calculate_strength_score("StrongP@ssw0rd!2024"), 100)
        self.assertEqual(calculate_strength_score(""), 0)
    
    def test_validate_password(self):
        """Test comprehensive password validation"""
        result = validate_password("SecureP@ss123")
        self.assertEqual(result['valid_length'], True)
        self.assertEqual(result['has_uppercase'], True)
        self.assertEqual(result['has_lowercase'], True)
        self.assertEqual(result['has_digits'], True)
        self.assertEqual(result['has_special_chars'], True)
        self.assertEqual(result['is_strong'], True)
        
        weak_result = validate_password("weak")
        self.assertEqual(weak_result['is_strong'], False)


if __name__ == '__main__':
    unittest.main()