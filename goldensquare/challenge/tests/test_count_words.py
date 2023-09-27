from lib.count_words import count_words

def test_counter_returns_two_given_hello_word():
    expected = 2
    actual = count_words('Hello, world!')
    assert actual == expected

def test_counter_returns_zero_for_empty_string():
    expected = 0
    actual = count_words('')
    assert actual == expected

def test_counter_works_given_long_string():
    expected = 20
    actual = count_words('one two three four five six, seven! eight nine 10 eleven doze thirteen3 fourt!een fiftenn sixtenn diciasete eighteen nineteen 20.')
    assert actual == expected