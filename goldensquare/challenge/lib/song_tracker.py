class MusicTracker():
    def __init__(self):
        self.song_list = []
    
    def add(self, song):
        if song in self.song_list:
            raise Exception("ERROR! SONG ALREADY IN LIST!")
        if not isinstance(song, str):
            song = str(song)
        if song.strip() != "":
            self.song_list.append(song)
    
    def list_of_songs(self):
        if self.song_list == []:
            raise Exception("ERROR! NO SONGS HERE YET!")
        message = "Songs you've listened to: "
        message += ", ".join(self.song_list)
        return message