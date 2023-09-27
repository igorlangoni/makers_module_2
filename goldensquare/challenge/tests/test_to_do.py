from lib.to_do import Todo

def test_given_task_adds_and_access_properties():
    task_1 = Todo('wash car')
    assert task_1.task == 'wash car'
    assert task_1.status == False

def test_given_task_mark_it_as_complete():
    task_1 = Todo('do homework')
    task_1.mark_complete()
    actual = task_1.status
    assert actual == True