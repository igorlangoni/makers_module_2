from lib.diary_method import make_snippet

def test_snippet_returns_five_words_and_elipsis_given_long_string():
    expected = 'Hello, my name is Lucy....'
    actual = make_snippet('Hello, my name is Lucy. Today is the 3rd of June')
    assert actual == expected

def test_snippet_returns_only_string_given_short_string():
    expected = 'Hi!'
    actual = make_snippet('Hi!')
    assert actual == expected

def test_snippet_returns_string_given_other_data_types():
    expected = 'True'
    actual = make_snippet(True)
    assert actual == expected