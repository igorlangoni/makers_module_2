class MusicLibrary():
    def __init__(self):
        self.tracks = []
    
    def add(self, track):
        self.tracks.append(track)
    
    def search_for_word(self, word):
        matching_list = []
        for track in self.tracks:
            if word in track.title:
                matching_list.append(track.title)
        return matching_list
    

class FakeSongLoveBySinger():
    def name_and_artirts():
        return ['Love', 'Singer']

class FakeSongCrazyByJames():
    def name_and_artirts():
        return ['Crazy', 'James']