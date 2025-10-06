"""
Password Strength Analyzer
This module contains functions to validate and analyze password strength.
"""

def check_length(password, min_length=8):
    """
    Checks if the password meets the minimum length requirement.
    
    Args:
        password (str): The password to check
        min_length (int): Minimum required length (default: 8)
    
    Returns:
        bool: True if password meets length requirement, False otherwise
    """
    return len(password) >= min_length


def has_uppercase(password):
    """
    Checks if the password contains at least one uppercase letter.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has uppercase letter, False otherwise
    """
    return any(char.isupper() for char in password)


def has_lowercase(password):
    """
    Checks if the password contains at least one lowercase letter.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has lowercase letter, False otherwise
    """
    return any(char.islower() for char in password)


def has_digits(password):
    """
    Checks if the password contains at least one digit.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has digit, False otherwise
    """
    return any(char.isdigit() for char in password)


def has_special_chars(password):
    """
    Checks if the password contains at least one special character.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has special character, False otherwise
    """
    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
    return any(char in special_characters for char in password)


def check_common_patterns(password):
    """
    Checks if the password contains common weak patterns.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password is safe (no common patterns), False if contains patterns
    """
    common_patterns = ['123', 'abc', 'password', 'qwerty', '111', '000']
    password_lower = password.lower()
    return not any(pattern in password_lower for pattern in common_patterns)


def calculate_strength_score(password):
    """
    Calculates the overall strength score of the password (0-100).
    
    Args:
        password (str): The password to evaluate
    
    Returns:
        int: Strength score from 0 to 100
    """
    # Return 0 for empty password
    if len(password) == 0:
        return 0
    
    score = 0
    
    # Length scoring (up to 30 points)
    if len(password) >= 8:
        score += 10
    if len(password) >= 12:
        score += 10
    if len(password) >= 16:
        score += 10
    
    # Character type scoring (15 points each)
    if has_uppercase(password):
        score += 15
    if has_lowercase(password):
        score += 15
    if has_digits(password):
        score += 15
    if has_special_chars(password):
        score += 15
    
    # Pattern check (10 points)
    if check_common_patterns(password):
        score += 10
    
    return min(score, 100)


def validate_password(password):
    """
    Combines all validation checks and returns a comprehensive report.
    
    Args:
        password (str): The password to validate
    
    Returns:
        dict: A dictionary containing all validation results and strength score
    """
    return {
        'valid_length': check_length(password),
        'has_uppercase': has_uppercase(password),
        'has_lowercase': has_lowercase(password),
        'has_digits': has_digits(password),
        'has_special_chars': has_special_chars(password),
        'no_common_patterns': check_common_patterns(password),
        'strength_score': calculate_strength_score(password),
        'is_strong': calculate_strength_score(password) >= 70
    }