def grammar_check(text):
    punctuation_list = ['.', '!', '?']
    if text[0].isupper() and text[-1] in punctuation_list:
        return True
    else:
        return False