class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.read_so_far_index = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        entry_word_count = len(self.contents.split())
        return entry_word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        entry_reading_time = self.count_words()/wpm
        return entry_reading_time

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        readable_chunk = wpm * minutes
        start_point = self.read_so_far_index
        end_point = self.read_so_far_index + readable_chunk
        self.read_so_far_index = end_point
        if end_point > self.count_words():
            self.read_so_far_index = 0
        
        formatted_chunk = ' '.join(self.contents.split()[start_point:end_point])
        return formatted_chunk