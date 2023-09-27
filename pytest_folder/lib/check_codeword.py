def check_codeword(codeword):
    if codeword == "horse":
        return "Correct! Come in"
    elif codeword[0] == 'h' and codeword[-1] == 'e':
        return 'Close, but nope.'
    else:
        return 'WRONG!'