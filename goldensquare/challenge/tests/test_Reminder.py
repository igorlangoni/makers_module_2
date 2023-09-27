from lib.Reminder import *
import pytest

def test_given_name_and_task_reminds_user_to_do_task():
    reminder = Reminder("Igor")
    reminder.remind_me_to("buy the tools")
    actual = reminder.remind()
    expected = 'Igor, you need to: buy the tools'
    assert actual == expected

def test_raises_exception_given_name_but_no_task():
    reminder = Reminder("Igor")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_msg = str(e.value)
    actual = error_msg
    expected = "NO TASKS SET"
    assert actual == expected

def test_accepts_name_but_empty_task():
    reminder = Reminder("Igor")
    reminder.remind_me_to("")
    actual = reminder.remind()
    expected = "Igor, you need to: "
    assert actual == expected

def test_returns_correct_list_of_multiple_tasks():
    reminder = Reminder("Igor")
    reminder.remind_me_to('wash the car')
    reminder.remind_me_to('take out the trash')
    reminder.remind_me_to('call the utility company')
    actual = reminder.remind()
    expected = "Igor, you need to: wash the car, take out the trash, call the utility company"
    assert actual == expected

def test_returns_correct_list_of_multiple_tasks_after_completing_one():
    reminder = Reminder("Igor")
    reminder.remind_me_to('wash the car')
    reminder.remind_me_to('take out the trash')
    reminder.remind_me_to('call the utility company')
    reminder.complete('wash the car')
    actual = reminder.remind()
    expected = "Igor, you need to: take out the trash, call the utility company"
    assert actual == expected

def test_returns_correct_list_given_multiple_tasks_multiple_completions():
    reminder = Reminder("Igor")
    reminder.remind_me_to('wash the car')
    reminder.remind_me_to('take out the trash')
    reminder.remind_me_to('call the utility company')
    reminder.complete('wash the car')
    reminder.remind_me_to('wash the car')
    reminder.complete('take out the trash')
    reminder.complete('call the utility company')
    actual = reminder.remind()
    expected = "Igor, you need to: wash the car"
    assert actual == expected

def test_raises_error_after_completing_all_task():
    reminder = Reminder("Igor")
    reminder.remind_me_to('wash the car')
    reminder.remind_me_to('take out the trash')
    reminder.remind_me_to('call the utility company')
    reminder.complete('wash the car')
    reminder.complete('take out the trash')
    reminder.complete('call the utility company')
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_msg = str(e.value)
    actual = error_msg
    expected = "NO TASKS SET"
    assert actual == expected

def test_returns_error_completing_non_existent_task():
    reminder = Reminder("Igor")
    reminder.remind_me_to('wash the car')
    with pytest.raises(Exception) as e:
        reminder.complete('take out the trash')
    error_msg = str(e.value)
    actual = error_msg
    expected = 'NON EXISTENT TASK'
    assert actual == expected
    

