class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        formatted_string = self.title.title() + ': ' + self.contents.capitalize()
        return formatted_string

    def count_words(self):
        number_words = len(self.contents.split())
        return number_words

    def reading_time(self, wpm):
        number_words = self.count_words()
        read_time = int(number_words/wpm)
        return read_time

    def reading_chunk(self, wpm, minutes):
        number_of_words = wpm*minutes
        start_point = self.read_so_far
        end_point = self.read_so_far + number_of_words
        chunk_list = self.contents.split()[start_point:end_point]
        chunk = ' '.join(chunk_list)
        self.read_so_far = end_point
        if end_point >= self.count_words():
            self.read_so_far = 0
            # start_point = self.read_so_far
            # end_point = self.read_so_far + number_of_words
        print(chunk)
        return chunk
    
diary = DiaryEntry('Ipsum Lorem', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus tincidunt nunc, sed semper neque posuere ut. Proin interdum vehicula neque vel gravida. Nullam rhoncus faucibus faucibus. Morbi eget dui vel ligula tristique sagittis. Vestibulum aliquam nibh dolor, in faucibus justo consequat sit amet. Sed at neque sed enim ultrices placerat. Integer suscipit mollis felis, eget eleifend tortor molestie sit amet. Donec non condimentum mi, et lacinia ante. Fusce non metus eleifend, fringilla tortor nec, iaculis orci. Etiam fringilla nulla sodales, mollis sapien at, aliquam tortor. Integer cursus ante lectus, eget pretium justo egestas eu. Quisque venenatis mi a urna viverra, nec vulputate ipsum hendrerit. Nullam laoreet feugiat ante ac finibus.')
diary.reading_chunk(3, 3)
diary.reading_chunk(5, 1)
diary.reading_chunk(4, 2)
diary.reading_chunk(30, 5)
diary.reading_chunk(2, 4)
diary.reading_chunk(3, 2)
print(diary.format())
print(diary.count_words())
print(diary.reading_time(30))
