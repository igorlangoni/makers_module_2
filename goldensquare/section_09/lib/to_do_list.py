class TodoList:
    def __init__(self):
        self.task_list = []

    def add(self, task):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.task_list.append(task)
    
    def all_tasks_status(self):
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_tasks = [task for task in self.task_list if task.status == False]
        return incomplete_tasks

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        completed_tasks = [task for task in self.task_list if task.status == True]
        return completed_tasks

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.task_list:
            task.mark_complete()