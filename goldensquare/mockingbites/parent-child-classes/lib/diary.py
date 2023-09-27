class Diary():
    def __init__(self, contents):
        # contents is a string
        self.contents = contents

    def read(self):
        # Returns the contents of the diary
        return self.contents