class GrammarStats:
    def __init__(self):
        self.punct_list = [ '.', '!', '?']
        self.total_texts = 0
        self.formatted = 0
  
    def check(self, text):
        first_letter = text[0]
        last_letter = text[-1]
        self.total_texts += 1
        if first_letter.isupper() and last_letter in self.punct_list:
            self.formatted += 1
            return True
        else:
            return False
        
  
    def percentage_good(self):
        percentage = int(self.formatted/self.total_texts*100)
        return percentage