from lib.counter import Counter

def test_counter_initial_count_is_zero():
    counter = Counter()
    result = counter.report()
    assert result == 'Counted to 0 so far.'

def test_counter_add_five_first_time():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_adding_negative_number():
    counter = Counter()
    counter.add(-10)
    result = counter.report()
    assert result == "Counted to -10 so far."

def test_counter_adding_multiple_numbers():
    counter = Counter()
    counter.add(3)
    counter.add(9)
    assert counter.report() == "Counted to 12 so far."

def test_counter_add_multiple_negative_numbers():
    counter = Counter()
    counter.add(-4)
    counter.add(-7)
    result = counter.report()
    assert result == "Counted to -11 so far."