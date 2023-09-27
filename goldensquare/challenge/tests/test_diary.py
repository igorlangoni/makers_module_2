from lib.diary import Diary

def test_initializing_returns_empty_list():
    diary = Diary()
    actual = diary.all()
    assert actual == []