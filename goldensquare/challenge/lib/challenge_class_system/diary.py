class Diary():
    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)
    
    def show_list(self):
        return self.entry_list
    
    def best_entry_to_read(self, wpm, minute):
        readable_words = wpm * minute
        possible_entries = [entry for entry in self.entry_list if entry.count_words() < readable_words]
        return(sorted(possible_entries, key = lambda entry : len(entry.contents))[-1])
    
    def show_all_phone_numbers(self):
        phone_list = []
        for entry in self.entry_list:
            for contact in entry.contact_list:
                phone_list.append(contact.phone_number)
        return phone_list