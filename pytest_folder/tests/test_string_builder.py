import pytest
from lib.string_builder import *

def test_error_msg_no_string_added():
    test_str = StringBuilder()
    with pytest.raises(Exception) as e:
        test_str.size()
    error_msg = str(e.value)
    assert error_msg == "No string added yet."

def test_adding_multiple_strings_outputs_concatenated_strings():
    test_str = StringBuilder()
    test_str.add('Hello')
    test_str.add(', ')
    test_str.add('world!')
    result = test_str.output()
    assert result == 'Hello, world!'

def test_size_multiple_strings_returns_len_strings():
    test_str = StringBuilder()
    test_str.add('Eu')
    test_str.add(' me chamo ')
    test_str.add('José!')
    result = test_str.size()
    assert result == 17



