from lib.greet import *

def test_greet_returns_hello_for_mark():
    result = greet('Mark')
    assert result == 'Hello, Mark!'