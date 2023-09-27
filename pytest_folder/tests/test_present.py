import pytest
from lib.present import Present

def test_wrapping_single_present():
    present = Present()
    result = present.wrap('toys')
    assert result == None

def test_wrapping_and_unwrapping_single_present():
    present = Present()
    present.wrap('toys')
    result = present.unwrap()
    assert result == None

def test_error_message_for_wrapping_multiple_presents():
    present = Present()
    present.wrap('toys')
    with pytest.raises(Exception) as e:
        present.wrap('books')
    error_msg = str(e.value)
    assert error_msg == "A content has already been wrapped."

def test_error_message_unwrapping_with_no_wrapped_presents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_msg = str(e.value)
    assert error_msg == 'No contents have been wrapped.'

def test_wrapping_unwrapping_multiple_presents():
    present = Present()
    present.wrap('action figure')
    present.unwrap()
    present.wrap('video-game')
    present.unwrap()
    result = present.wrap('phone')
    assert result == None

