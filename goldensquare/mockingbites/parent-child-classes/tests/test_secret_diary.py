from lib.secret_diary import SecretDiary
from unittest.mock import Mock

def test_reading_locked_diary():
    fake_entry = Mock()
    fake_entry.contents = 'Hello, my name is Jane'
    s_diary = SecretDiary(fake_entry)
    assert s_diary.read() == 'Go away!'

def test_reading_unlocked_diary():
    fake_entry = Mock()
    fake_entry.contents = 'Hello, my name is Jane'
    s_diary = SecretDiary(fake_entry)
    s_diary.unlock()
    assert s_diary.read() == 'Hello, my name is Jane'

def test_unlocking_and_locking_returns_true():
    fake_entry = Mock()
    fake_entry.contents = 'Hello'
    s_diary = SecretDiary(fake_entry)
    s_diary.unlock()
    s_diary.lock()
    assert s_diary.locked_status == True
    assert s_diary.contents == 'Hello'