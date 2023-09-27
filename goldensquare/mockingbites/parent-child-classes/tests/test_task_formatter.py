from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

def test_given_complete_task_returns_x_title():
    fake_task = Mock()
    fake_task.complete_status = True
    fake_task.title = 'Homework'
    formatter = TaskFormatter(fake_task)
    assert formatter.format() == f"[x] {fake_task.title}"

def test_given_incomplete_task_returns_empty_title():
    fake_task = Mock()
    fake_task.complete_status = False
    fake_task.title = 'Wash car'
    formatter = TaskFormatter(fake_task)
    assert formatter.format() == '[ ] Wash car'