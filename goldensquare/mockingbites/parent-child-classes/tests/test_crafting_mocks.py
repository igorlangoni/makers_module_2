import pytest
from unittest.mock import Mock


def test_set_up_blank_mock():
    # Uncomment and set up your mocks here
    fake_object = Mock()
    assert fake_object is not None


def test_set_up_mock_with_methods():
    # Uncomment and set up your mocks here
    fake_object = Mock()
    fake_object.speak.return_value = "Meow, Jess"
    fake_object.count_ears.return_value = 2
    fake_object.count_legs.return_value = 4
    # Don't edit below
    assert fake_object.speak("Jess") == "Meow, Jess"
    assert fake_object.count_ears() == 2
    assert fake_object.count_legs() == 4



def test_assert_that_mock_was_called():
    fake_object = Mock()
    fake_object.speak("Steve")
    # Write an assertion below that the method "speak" was called with
    # the argument "Steve"
    fake_object.speak.assert_called_with("Steve") #assert is not called in the beggining, but in the middle

def test_creates_mock_for_specific_case():
    fake_diary = Mock()

    # Set up this mock to pass the tests below
    fake_diary.count_entries.return_value = 2
    

    # Don't edit below
    fake_diary.add(Mock())
    fake_diary.add(Mock())
    assert fake_diary.count_entries() == 2

def test_creates_a_sophisticated_mock():
    # Uncomment and set up your mocks here
    task_list = Mock()
    task =  Mock()
    task_list.list.return_value = [task]
    task_list.count.return_value = 1
    task_list.clear.return_value = "success"
    # Don't edit below
    task_list.add(task)
    assert task_list.list() == [task]
    assert task_list.count() == 1
    assert task_list.clear() == "success"
