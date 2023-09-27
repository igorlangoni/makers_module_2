from lib.task_tracker import task_tracker
import pytest

def test_returns_true_given_string_with_todo():
    expected = True
    actual = task_tracker('Groceries #TODO')
    assert actual == expected

def test_returns_false_given_string_without_todo():
    expected = False
    actual = task_tracker("It's a beautiful day! #BLESSED")
    assert actual == expected

def test_returns_false_given_lowercase_todo():
    expected = False
    actual = task_tracker("Do the laundry #todo")
    assert actual == expected

def test_returns_false_given_wrong_spec_char():
    expected = False
    actual = task_tracker("Pick-up kids from school *TODO")
    assert actual == expected

def test_raises_error_given_empty_string():
    with pytest.raises(Exception) as e:
        task_tracker("")
    error_msg = str(e.value)
    assert error_msg == "ERROR! CANNOT ACCEPT EMPTY STRING!"