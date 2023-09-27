from lib.gratitudes import Gratitudes

def test_initial_str_is_empty():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == 'Be grateful for: '

def test_adding_single_gratitude():
    grateful = Gratitudes()
    grateful.add('my family')
    result = grateful.format()
    assert result == "Be grateful for: my family"

def test_adding_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add('god')
    gratitudes.add('my money')
    gratitudes.add('my dog')
    result = gratitudes.format()
    assert result == 'Be grateful for: god, my money, my dog'