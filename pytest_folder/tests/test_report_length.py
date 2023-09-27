from lib.report_length import *

def test_report_length_says_six_for_hello():
    result = report_length('Hello!')
    assert result == 'This string was 6 characters long.'

def test_report_length_says_sixteen_for_my_name_is_Igor():
    result = report_length('My name is Igor.')
    assert result == 'This string was 16 characters long.'

def test_report_length_says_zero_for_empty_string():
    result = report_length('')
    assert result == 'This string was 0 characters long.'
