class Diary():
        #PUBLIC PROPERTIES
                # entry_list

        def __init__(self):
                pass

        def add(self, entry):
                #PARAMETERS
                        # entry - an instance of DiaryEntry
                #RETURNS
                        # nothing
                #SIDE EFFECTS
                        # adds an entry to the list
        
        def show_list(self):
                #PARAMETERS
                        # nothing
                #RETURNS
                        # entry_list
                #SIDE EFFECTS
                        # nothing
        
        def best_entry_to_read(self, wpm, minute):
                 #PARAMETERS
                        # wpm - reading speed, int
                        # minute - available reading time in minutes, int
                #RETURNS
                        # an instance of entry which has a reading time close to wpm*minute, but not over.
                #SIDE EFFECTS
                        # nothin

class DiaryEntry():
        #PUBLIC PROPERTIES
                #title
                #contents
                #contact_list

        def __init__(self, title, contents):
                 #PARAMETERS
                        # title
                        # contents   
                #RETURNS
                        # nothing
                #SIDE EFFECTS
                        # nothing
        
        def add(self, contact):
                 #PARAMETERS
                        # contact - an instance of Contact
                #RETURNS
                        # nothing
                #SIDE EFFECTS
                        # adds a contact to the contact_list 

def Contact():
        #PUBLIC PROPERTIES
                #name
                #phone_number
        def __init__(self, name, phone_number):
                pass

def ToDoList():
        def __init__(self):

        def add(self, task):
                 #PARAMETERS
                        # task - an instance of Todo
                #RETURNS
                        # nothing
                #SIDE EFFECTS
                        # adds a task to the task_list

def ToDo():
        def __init__(self, task):
                 #PARAMETERS
                        # task - a string representing a task
                #RETURNS
                        # nothing
                #SIDE EFFECTS
                        # nothin
        