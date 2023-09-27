from unittest.mock import Mock
from lib.music_library import MusicLibrary

def test_adding_tracks():
    music_library = MusicLibrary()
    fakematchinsong = Mock()
    music_library.add(fakematchinsong)
    fakenotmatchingsong = Mock()
    music_library.add(fakenotmatchingsong)
    assert music_library == [fakematchinsong, fakenotmatchingsong]

