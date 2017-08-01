

class Artist:

    def __init__(self, name, uri):

        self.name = name
        self.uri = uri

    def __repr__(self):
        return str.format("{}|{}", self.name, self.uri)
