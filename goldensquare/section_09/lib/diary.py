class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        diary_total_words = 0
        for entry in self.entries:
            diary_total_words += entry.count_words()
        return diary_total_words

    def reading_time(self, wpm):
        diary_total_reading_time = self.count_words()/wpm
        return diary_total_reading_time
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        readable_chunk = wpm * minutes
        best_entry = None
        for entry in self.all():
            if entry.count_words() > readable_chunk:
                continue
            elif best_entry == None:
                best_entry = entry
            elif entry.count_words() > best_entry.count_words():
                best_entry = entry
        return best_entry.title

        