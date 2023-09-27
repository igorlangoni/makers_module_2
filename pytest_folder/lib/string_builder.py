class StringBuilder:
    def __init__ (self):
        self.str = ""
    
    def add(self, phrase):
        self.str += phrase
    
    def size(self):
        if self.str == '':
            raise Exception("No string added yet.")
        return len(self.str)
    
    def output(self):
        return self.str