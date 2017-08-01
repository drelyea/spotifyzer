

class Album:

    def __init__(self, name, artist, uri):

        self.name = name
        self.artist = artist
        self.uri = uri

    def __repr__(self):
        return str.format("{}|{}|{}", self.name, self.artist, self.uri)
