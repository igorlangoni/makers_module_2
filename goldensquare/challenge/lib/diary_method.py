def make_snippet(string):
    w_list = str(string).split()
    if len(w_list) > 5:
        string = ' '.join(w_list[:5]) + '...'
        return string
    
    else:
         return str(string)