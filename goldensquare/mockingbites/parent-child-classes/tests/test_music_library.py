from lib.music_library import MusicLibrary
from unittest.mock  import Mock

def test_initialises_empty_list():
    library = MusicLibrary()
    assert library.track_list == []

def test_we_can_add_tracks_and_show_in_a_list():
    library = MusicLibrary()
    fake_track = Mock()
    library.add(fake_track)
    assert library.track_list == [fake_track]

def test_search_returns_list_with_tracks_containing_word():
    library = MusicLibrary()
    fake_track_1 = Mock()
    fake_track_1.matches.return_value = True
    fake_track_2 = Mock()
    fake_track_2.matches.return_value = False
    library.add(fake_track_1)
    library.add(fake_track_2)
    assert library.search('T') == [fake_track_1]