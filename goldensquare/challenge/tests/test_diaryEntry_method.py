from lib.diaryEntry_method import *

def test_format_returns_formatted_entry():
    diary = DiaryEntry('my title', 'these are the contents')
    actual = diary.format()
    expected = 'My Title: These are the contents'
    assert actual == expected

def test_format_returns_formatted_given_mixed_cases():
    diary = DiaryEntry('My tITLe', 'ThESE Are THE CONTEnts')
    actual = diary.format()
    expected = 'My Title: These are the contents'
    assert actual == expected

def test_count_words_returns_four_given_contents():
    diary = DiaryEntry('My title', 'These are the Contents')
    actual = diary.count_words()
    expected = 4
    assert actual == expected

def test_reading_time_returns_ten_given_wpm():
    diary = DiaryEntry('My title', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus tincidunt nunc, sed semper neque posuere ut. Proin interdum vehicula neque vel gravida. Nullam rhoncus faucibus faucibus. Morbi eget dui vel ligula tristique sagittis. Vestibulum aliquam nibh dolor, in faucibus justo consequat sit amet. Sed at neque sed enim ultrices placerat. Integer suscipit mollis felis, eget eleifend tortor molestie sit amet. Donec non condimentum mi, et lacinia ante. Fusce non metus eleifend, fringilla tortor nec, iaculis orci. Etiam fringilla nulla sodales, mollis sapien at, aliquam tortor. Integer cursus ante lectus, eget pretium justo egestas eu. Quisque venenatis mi a urna viverra, nec vulputate ipsum hendrerit. Nullam laoreet feugiat ante ac finibus.')
    actual = diary.reading_time(5)
    expected = 22
    assert actual == expected

def test_chunk_returns_correct_words_given_first_chunk():
    diary = DiaryEntry('My title', "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus tincidunt nunc, sed semper neque posuere ut. Proin interdum vehicula neque vel gravida. Nullam rhoncus faucibus faucibus. Morbi eget dui vel ligula tristique sagittis. Vestibulum aliquam nibh dolor, in faucibus justo consequat sit amet. Sed at neque sed enim ultrices placerat. Integer suscipit mollis felis, eget eleifend tortor molestie sit amet. Donec non condimentum mi, et lacinia ante. Fusce non metus eleifend, fringilla tortor nec, iaculis orci. Etiam fringilla nulla sodales, mollis sapien at, aliquam tortor. Integer cursus ante lectus, eget pretium justo egestas eu. Quisque venenatis mi a urna viverra, nec vulputate ipsum hendrerit. Nullam laoreet feugiat ante ac finibus.")
    actual = diary.reading_chunk(3, 8)
    expected = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus tincidunt nunc, sed semper neque posuere ut. Proin interdum vehicula neque vel gravida. Nullam'
    assert actual == expected

def test_chunk_returns_correct_given_multiple_chunks():
    diary = DiaryEntry('My title', "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus tincidunt nunc, sed semper neque posuere ut. Proin interdum vehicula neque vel gravida. Nullam rhoncus faucibus faucibus. Morbi eget dui vel ligula tristique sagittis. Vestibulum aliquam nibh dolor, in faucibus justo consequat sit amet. Sed at neque sed enim ultrices placerat. Integer suscipit mollis felis, eget eleifend tortor molestie sit amet. Donec non condimentum mi, et lacinia ante. Fusce non metus eleifend, fringilla tortor nec, iaculis orci. Etiam fringilla nulla sodales, mollis sapien at, aliquam tortor. Integer cursus ante lectus, eget pretium justo egestas eu. Quisque venenatis mi a urna viverra, nec vulputate ipsum hendrerit. Nullam laoreet feugiat ante ac finibus.")
    diary.reading_chunk(10, 4)
    actual = diary.reading_chunk(10, 4)
    expected = "justo consequat sit amet. Sed at neque sed enim ultrices placerat. Integer suscipit mollis felis, eget eleifend tortor molestie sit amet. Donec non condimentum mi, et lacinia ante. Fusce non metus eleifend, fringilla tortor nec, iaculis orci. Etiam fringilla nulla"
    assert actual == expected

def test_chunk_returns_beggining_of_string():
    diary = DiaryEntry('My title', "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus tincidunt nunc, sed semper neque posuere ut. Proin interdum vehicula neque vel gravida. Nullam rhoncus faucibus faucibus. Morbi eget dui vel ligula tristique sagittis. Vestibulum aliquam nibh dolor, in faucibus justo consequat sit amet. Sed at neque sed enim ultrices placerat. Integer suscipit mollis felis, eget eleifend tortor molestie sit amet. Donec non condimentum mi, et lacinia ante. Fusce non metus eleifend, fringilla tortor nec, iaculis orci. Etiam fringilla nulla sodales, mollis sapien at, aliquam tortor. Integer cursus ante lectus, eget pretium justo egestas eu. Quisque venenatis mi a urna viverra, nec vulputate ipsum hendrerit. Nullam laoreet feugiat ante ac finibus.")
    diary.reading_chunk(10, 4)
    diary.reading_chunk(10, 4)
    actual = diary.reading_chunk(10, 4)
    expected = 'sodales, mollis sapien at, aliquam tortor. Integer cursus ante lectus, eget pretium justo egestas eu. Quisque venenatis mi a urna viverra, nec vulputate ipsum hendrerit. Nullam laoreet feugiat ante ac finibus.'
    assert actual == expected
