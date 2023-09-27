class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.contact_list = []
    
    def add_contact(self, contact):
        self.contact_list.append(contact)
    
    def count_words(self):
        entry_total_words = len(self.contents.split())
        return entry_total_words
    
    def show_contacts(self):
        return self.contact_list