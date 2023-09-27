from lib.check_codeword import *

def test_check_codeword_says_correct_for_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in"

def test_check_codeword_says_close_for_home():
    result = check_codeword('home')
    assert result == 'Close, but nope.'

def test_check_codeword_says_wrong_for_cow():
    result = check_codeword('cow')
    assert result == 'WRONG!'
