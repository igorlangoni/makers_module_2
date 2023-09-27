class Present():
    def __init__(self):
        self.contents = None
    
    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A content has already been wrapped.")
        self.contents = contents
    
    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        self.contents = None