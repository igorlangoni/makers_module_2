class TodoList():
    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task_list.append(task)

    def show_tasks(self):
        return self.task_list