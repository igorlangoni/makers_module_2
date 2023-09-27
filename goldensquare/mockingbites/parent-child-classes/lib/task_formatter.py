class TaskFormatter():
    def __init__(self, task): # task is an instance of Task
        self.task_title = task.title
        self.complete_status = task.complete_status

    def format(self):
        # Returns the task formatted as a string.
        # If the task is not complete, the format is:
        # - [ ] Task title
        # If the task is complete, the format is:
        # - [x] Task title
        if self.complete_status == True:
            return f"[x] {self.task_title}"
        return f"[ ] {self.task_title}"