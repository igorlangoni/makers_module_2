from lib.planner import Planner
from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.to_do_list import TodoList
from lib.to_do import Todo

def test_scrapes_diary_for_phone_numbers():
    planner = Planner()
    diary = Diary()
    entry1 = DiaryEntry('Title1', 'Contents 1234-6789')
    entry2 = DiaryEntry('Title2', 'Contents hello world')
    diary.add(entry1)
    diary.add(entry2)
    planner.add(diary)
    assert planner.list_of_contacts(diary) == ["1234-6789"]

    

