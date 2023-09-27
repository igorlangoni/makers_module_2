class Track():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def format(self):
        return f"{self.title.upper()} by {self.artist.upper()}"
    
    def matches(self, keyword):
        return keyword in self.title or keyword in self.artist
        
