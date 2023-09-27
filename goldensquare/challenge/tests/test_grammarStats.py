from lib.grammarStats import GrammarStats

def test_check_returns_true_given_formatted_string():
    text = GrammarStats()
    actual = text.check('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc faucibus semper augue eget dapibus. Praesent lobortis vestibulum ligula, non interdum ligula laoreet a. In quis neque sapien. Donec id sodales tortor, ut imperdiet risus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum eu porttitor orci, ac pretium lorem. Fusce ante elit, aliquam vitae velit non, tempus maximus neque. In porttitor at purus vitae consectetur. Sed auctor aliquet quam, a sodales magna congue non. Curabitur porttitor metus libero, vitae semper nulla lobortis eu. Pellentesque eu arcu vitae sem consequat lobortis id et erat. Morbi nec ex quis lorem sagittis malesuada. Phasellus neque sem, venenatis id tempor auctor, tristique nec nisl.')
    expected = True
    assert actual == expected

def test_check_returns_false_given_upper_but_not_punctuation():
    text = GrammarStats()
    actual = text.check('Hello, world')
    expected = False
    assert actual == expected

def test_check_returns_false_given_lower_and_punctuation():
    text = GrammarStats()
    actual = text.check('hello, World!')
    expected = False
    assert actual == expected

def test_returns_hundred_percent_given_only_formatted_texts():
    text = GrammarStats()
    text.check('Hello, world!')
    text.check('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc faucibus semper augue eget dapibus. Praesent lobortis vestibulum ligula, non interdum ligula laoreet a. In quis neque sapien. Donec id sodales tortor, ut imperdiet risus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum eu porttitor orci, ac pretium lorem. Fusce ante elit, aliquam vitae velit non, tempus maximus neque. In porttitor at purus vitae consectetur. Sed auctor aliquet quam, a sodales magna congue non. Curabitur porttitor metus libero, vitae semper nulla lobortis eu. Pellentesque eu arcu vitae sem consequat lobortis id et erat. Morbi nec ex quis lorem sagittis malesuada. Phasellus neque sem, venenatis id tempor auctor, tristique nec nisl.')
    actual = text.percentage_good()
    expected = 100
    assert actual == expected

def test_percentage_returns_sixty_given_3_correct_2_wrong():
    text = GrammarStats()
    text.check('hi, my friend?')
    text.check('My name is Igor.')
    text.check('I am 30 years old!')
    text.check('I like pokemon;')
    text.check('Bye!')
    actual = text.percentage_good()
    expected = 60
    assert actual == expected