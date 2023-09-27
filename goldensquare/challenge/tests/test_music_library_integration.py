from lib.music_library import MusicLibrary
from lib.track  import Track

def test_adding_two_tracks_returns_in_track_list():
    library = MusicLibrary()
    track_1 = Track('Patience', "Guns n' Roses")
    track_2 = Track('Its my life', "Bon Jovi")
    library.add(track_1)
    library.add(track_2)
    actual = library.tracks
    assert actual == [track_1, track_2]

def test_searching_for_word_returns_matching_track():
    library = MusicLibrary()
    track_1 = Track('Patience life', "Guns n' Roses")
    track_2 = Track('Its my life', "Bon Jovi")
    library.add(track_1)
    library.add(track_2)
    actual = library.search_for_word('life')
    assert actual == [track_1.title, 'Its my life']

def test_searching_for_partial_word_returns_track():
    library = MusicLibrary()
    track_1 = Track('Patience life', "Guns n' Roses")
    track_2 = Track('Its my life', "Bon Jovi")
    library.add(track_1)
    library.add(track_2)
    actual = library.search_for_word('ence')
    assert actual == ['Patience life']

def test_returns_empty_street_for_word_not_in_track():
    library = MusicLibrary()
    track_1 = Track('Patience life', "Guns n' Roses")
    track_2 = Track('Its my life', "Bon Jovi")
    library.add(track_1)
    library.add(track_2)
    actual = library.search_for_word('joia')
    assert actual == []

def test_returns_formatted_track_string():
    library = MusicLibrary()
    track_1 = Track('Patience life', "Guns n' Roses")
    track_2 = Track('Its my life', "Bon Jovi")
    library.add(track_1)
    library.add(track_2)
    assert track_1.format() == "PATIENCE LIFE by GUNS N' ROSES"
    assert track_2.format() == "ITS MY LIFE by BON JOVI"