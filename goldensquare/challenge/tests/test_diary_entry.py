from lib.diary_entry import DiaryEntry

def test_adding_title_and_contents_and_accessing_them():
    entry_1 = DiaryEntry('Title', 'Contents goodbye')
    assert entry_1.title == 'Title'
    assert entry_1.contents == 'Contents goodbye'

def test_given_entry_returns_total_words():
    entry_1 = DiaryEntry('Title', 'one two three four five')
    actual = entry_1.count_words()
    assert actual == 5

def test_given_wpm_returns_reading_time():
    entry_1 = DiaryEntry('Title', '1 2 3 4 5 6 7 8 9 10')
    actual = entry_1.reading_time(2)
    assert actual == 5

def test_given_wpm_and_minutes_returns_readable_chunk():
    entry_1 = DiaryEntry('Title', '1 2 3 4 5 6 7 8 9 10')
    actual = entry_1.reading_chunk(2, 4)
    assert actual == '1 2 3 4 5 6 7 8'

def test_given_multiple_chunks_returns_following_words_until_last():
    entry_1 = DiaryEntry('Title', '1 2 3 4 5 6 7 8 9 10')
    entry_1.reading_chunk(2, 2)
    entry_1.reading_chunk(1, 1)
    actual = entry_1.reading_chunk(2,2)
    assert actual == '6 7 8 9'

def test_given_too_long_chunk_returns_up_to_last_word():
    entry_1 = DiaryEntry('Title', '1 2 3 4 5 6 7 8 9 10 11')
    entry_1.reading_chunk(2, 2)
    entry_1.reading_chunk(1, 1)
    actual = entry_1.reading_chunk(2,4)
    assert actual == '6 7 8 9 10 11'

def test_given_chunk_after_finishing_entry_starts_from_beggining():
    entry_1 = DiaryEntry('Title', '1 2 3 4 5 6 7 8 9 10 11')
    entry_1.reading_chunk(2, 2)
    entry_1.reading_chunk(3, 10)
    entry_1.reading_chunk(3, 3)
    entry_1.reading_chunk(2, 3)
    actual = entry_1.reading_chunk(1,3)
    assert actual == '1 2 3'
