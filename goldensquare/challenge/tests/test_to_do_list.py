from lib.to_do_list import TodoList

def test_initializing_returns_empty_list():
    todo_list = TodoList()
    assert todo_list.task_list == []