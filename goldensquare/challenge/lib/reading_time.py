def reading_time(number_words):
    if isinstance(number_words, float):
        time_taken = int(number_words/200)
        answer = f"{time_taken} minutes"
        return answer
    
    elif not isinstance(number_words, int):
        return False

    elif number_words < 0:
        return False  
    else:
        time_taken = int(number_words/200)
        answer = f"{time_taken} minutes"
        return answer
