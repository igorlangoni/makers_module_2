from lib.reading_time import reading_time

def test_reading_time_returns_two_given_four_hundred():
    expected = '2 minutes'
    actual = reading_time(400)
    assert expected == actual

def test_reading_time_returns_false_for_negative():
    expected = False
    actual = reading_time(-150)
    assert expected == actual

def test_reading_time_return_rounded_given_decimal():
    expected = '2 minutes'
    actual = reading_time(400.05)
    assert expected == actual

def test_return_false_given_not_integer():
    expected = False
    actual = reading_time('hello world')
    assert actual == expected