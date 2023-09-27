from lib.music_library import MusicLibrary
from lib.track import Track

def test_we_can_add_tracks_and_show_in_list():
    library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    library.add(track_1)
    assert library.track_list == [track_1]

def test_search_returns_list_with_tracks_containing_word():
    library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    track_2 = Track('Title2', 'Artist2')
    library.add(track_1)
    library.add(track_2)
    assert library.search('T') == [track_1, track_2]