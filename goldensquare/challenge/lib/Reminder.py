class Reminder():
    def __init__(self, name):
        self.name = name
        self.to_do_list = []

    def remind_me_to(self, task):
        self.to_do_list.append(task)
    
    def remind(self):
        if self.to_do_list == []:
            raise Exception("NO TASKS SET")
        remind = f"{self.name}, you need to: "
        remind += ', '.join(self.to_do_list)
        return remind
    
    def complete(self, task):
        if task not in self.to_do_list:
            raise Exception('NON EXISTENT TASK')
        self.to_do_list.remove(task)