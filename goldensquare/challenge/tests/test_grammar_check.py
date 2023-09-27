from lib.grammar_check import grammar_check

def test_check_returns_true_for_Hello_world():
    expected = True
    actual = grammar_check('Hello, world!')
    assert expected == actual

def test_check_returns_false_for_lower_case_word():
    expected = False
    actual = grammar_check('hi, my name is John.')
    assert expected == actual

def test_check_returns_false_for_wrong_punctuation():
    expected = False
    actual = grammar_check('I like milk, cheese,')
    assert expected == actual

def test_check_returns_false_given_no_punctuation():
    expected = False
    actual = grammar_check('Hello, world')
    assert expected == actual

