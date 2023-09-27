import pytest
from lib.password_checker import *

def test_checker_accepts_eight_characters():
    password_checker = PasswordChecker()
    result = password_checker.check('password')
    assert result == True

def test_checker_rejects_shorter_passwords():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('1234567')
    error_msg = str(e.value)
    assert error_msg == "Invalid password, must be 8+ characters."
    