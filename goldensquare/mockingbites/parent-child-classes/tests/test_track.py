from lib.track import Track

def test_initialise_track():
    track = Track('Title1', 'Artist 1')
    assert track.title == 'Title1'

def test_matches_returns_true_given_full_keyword():
    track = Track('Fireboy', 'David')
    assert track.matches('Fireboy') == True

def test_given_partial_word_returns_true():
    track = Track('Fireboy', 'David')
    assert track.matches('id') == True

def test_given_wrong_keyword_returns_false():
    track = Track('Fireboy', 'David')
    assert track.matches('Igor') == False