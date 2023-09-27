def task_tracker(text):
    if text == (""):
        raise Exception("ERROR! CANNOT ACCEPT EMPTY STRING!")
    return '#TODO' in text
       