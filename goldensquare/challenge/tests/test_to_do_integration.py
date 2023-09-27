from lib.to_do_list import TodoList
from lib.to_do import Todo

def test_given_todo_task_adds_and_return_list_with_them():
    todo_list = TodoList()
    task_1 = Todo('clean house')
    task_2 = Todo('wash dog')
    todo_list.add(task_1.task)
    todo_list.add(task_2.task)
    actual = todo_list.task_list
    assert actual == ["clean house", "wash dog"]

def test_returns_list_of_incomplete_tasks():
    todo_list = TodoList()
    task_1 = Todo('clean house')
    task_2 = Todo('wash dog')
    todo_list.add(task_1)
    todo_list.add(task_2)
    actual = todo_list.incomplete()
    assert actual == [task_1, task_2]

def test_returns_list_of_completed_tasks():
    todo_list = TodoList()
    task_1 = Todo('clean house')
    task_2 = Todo('wash dog')
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    actual = todo_list.complete()
    assert actual == [task_1, task_2]

def test_give_up_returns_all_task_as_completed():
    todo_list = TodoList()
    task_1 = Todo('clean house')
    task_2 = Todo('wash dog')
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.give_up()
    actual = todo_list.complete()
    assert actual == todo_list.task_list