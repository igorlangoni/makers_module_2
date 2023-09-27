from lib.diary import Diary

def test_reading_contents():
    entry = Diary('Hi, my names Goku')
    assert entry.read() == 'Hi, my names Goku'