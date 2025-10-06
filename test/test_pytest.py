"""
Pytest test suite for password_validator.py
"""
import pytest # type: ignore

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


def test_check_length():
    """Test password length validation"""
    assert check_length("12345678") == True
    assert check_length("1234567") == False
    assert check_length("") == False
    assert check_length("VeryLongPassword123!") == True


def test_has_uppercase():
    """Test uppercase letter detection"""
    assert has_uppercase("Password") == True
    assert has_uppercase("password") == False
    assert has_uppercase("PASSWORD") == True
    assert has_uppercase("Pass123!") == True


def test_has_lowercase():
    """Test lowercase letter detection"""
    assert has_lowercase("password") == True
    assert has_lowercase("PASSWORD") == False
    assert has_lowercase("Pass123!") == True
    assert has_lowercase("123456") == False


def test_has_digits():
    """Test digit detection"""
    assert has_digits("Pass123") == True
    assert has_digits("Password") == False
    assert has_digits("12345678") == True
    assert has_digits("Pass!@#") == False


def test_has_special_chars():
    """Test special character detection"""
    assert has_special_chars("Pass@123") == True
    assert has_special_chars("Password123") == False
    assert has_special_chars("!@#$%^&*") == True
    assert has_special_chars("SimplePass") == False


def test_check_common_patterns():
    """Test common pattern detection"""
    assert check_common_patterns("SecurePass!23") == True
    assert check_common_patterns("password123") == False
    assert check_common_patterns("qwerty456") == False
    assert check_common_patterns("MyP@ssw0rd") == True


def test_calculate_strength_score():
    """Test password strength score calculation"""
    assert calculate_strength_score("Pass@123") == 70
    assert calculate_strength_score("weak") == 25
    assert calculate_strength_score("StrongP@ssw0rd!2024") == 100
    assert calculate_strength_score("") == 0


def test_validate_password():
    """Test comprehensive password validation"""
    result = validate_password("SecureP@ss123")
    assert result['valid_length'] == True
    assert result['has_uppercase'] == True
    assert result['has_lowercase'] == True
    assert result['has_digits'] == True
    assert result['has_special_chars'] == True
    assert result['is_strong'] == True
    
    weak_result = validate_password("weak")
    assert weak_result['is_strong'] == False


# Parametrized tests (as mentioned in your document)
# These allow testing multiple scenarios with the same test function

@pytest.mark.parametrize("password,expected", [
    ("12345678", True),
    ("1234567", False),
    ("VeryLongPassword", True),
    ("short", False),
])
def test_check_length_parametrized(password, expected):
    """Parametrized test for length validation"""
    assert check_length(password) == expected


@pytest.mark.parametrize("password,expected_score", [
    ("Pass@123", 70),
    ("weak", 25),
    ("StrongP@ssw0rd!2024", 100),
    ("", 0),
    ("Simple123", 55),
])
def test_calculate_strength_score_parametrized(password, expected_score):
    """Parametrized test for strength score calculation"""
    assert calculate_strength_score(password) == expected_score