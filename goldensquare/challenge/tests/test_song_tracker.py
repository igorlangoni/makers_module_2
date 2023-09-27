from lib.song_tracker import *
import pytest

def test_added_song_is_returned_in_list():
    tracker = MusicTracker()
    tracker.add('Piano Man')
    actual = tracker.list_of_songs()
    expected = "Songs you've listened to: Piano Man"
    assert actual == expected

def test_doesnt_return_empty_string_in_list():
    tracker = MusicTracker()
    tracker.add('Imagine')
    tracker.add("    ")
    actual = tracker.list_of_songs()
    expected = "Songs you've listened to: Imagine"
    assert actual == expected

def test_raises_error_printing_empty_list():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.list_of_songs()
    error_msg = str(e.value)
    actual = error_msg
    expected = 'ERROR! NO SONGS HERE YET!'
    assert actual == expected

def test_raises_error_adding_repeated_song():
    tracker = MusicTracker()
    tracker.add('Like a Rolling Stone')
    tracker.add("Blowin' in the wind")
    with pytest.raises(Exception) as e:
        tracker.add("Blowin' in the wind")
    error_msg = str(e.value)
    actual = error_msg
    expected = 'ERROR! SONG ALREADY IN LIST!'
    assert actual == expected

def test_adds_str_of_wrong_type_to_list():
    tracker = MusicTracker()
    tracker.add(True)
    tracker.add(1984)
    actual = tracker.list_of_songs()
    expected = "Songs you've listened to: True, 1984"
    assert actual == expected
