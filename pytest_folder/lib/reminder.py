class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None
    
    def remind_me_to(self, task):
        self.task = task
    
    def remind(self):
        if self.task == None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"
    
    
    
