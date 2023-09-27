from lib.secret_diary import SecretDiary
from lib.diary import Diary

def test_reading_locked_diary():
    entry = Diary('Hello, my name is Jane')
    s_diary = SecretDiary(entry)
    assert s_diary.read() == 'Go away!'

def test_reading_unlocked_diary():
    entry = Diary('Hello, my name is Jane')
    s_diary = SecretDiary(entry)
    s_diary.unlock()
    assert s_diary.locked_status == False
    assert s_diary.read() == 'Hello, my name is Jane'

def test_unlocking_and_locking_returns_true():
    entry = Diary('Hello, my name is Jane')
    s_diary = SecretDiary(entry)
    s_diary.unlock()
    s_diary.lock()
    assert s_diary.locked_status == True