from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_given_two_entries_returns_them_in_list():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'Contents1 THe END!')
    entry_2 = DiaryEntry('Title2', 'Contents2 THE end!')
    diary.add(entry_1)
    diary.add(entry_2)
    actual = diary.all()
    assert actual == [entry_1, entry_2]

def test_given_multiple_entries_returns_total_words():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'Contents1 THe END!')
    entry_2 = DiaryEntry('Title2', 'Contents2 THE end!')
    diary.add(entry_1)
    diary.add(entry_2)
    actual = diary.count_words()
    assert actual == 6

def test_given_wpm_and_minutes_returns_full_diary_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'Contents1 THe END!')
    entry_2 = DiaryEntry('Title2', 'Contents2 THE end!')
    diary.add(entry_1)
    diary.add(entry_2)
    actual = diary.reading_time(2)
    assert actual == 3

def test_given_wpm_and_minutes_returns_closest_entry_in_number_of_words():
    diary = Diary()
    entry_1 = DiaryEntry('Title1', 'Contents1 is the biggest entry in the history THe END!')
    entry_2 = DiaryEntry('Title2', 'Contents2 small THE end!')
    entry_3 = DiaryEntry('Title3', 'Contents3 is the middle one the end!')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    actual = diary.find_best_entry_for_reading_time(2, 4)
    assert actual == 'Title3'