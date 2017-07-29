class Song:

    def __init__(self, name, artist, timestamp, song_id):
        self.name = name
        self.artist = artist
        self.timestamp = timestamp
        self.id = song_id + timestamp

    def __repr__(self):
        return str.format("{}: {} | {} | {}", self.id, self.name, self.artist, self.timestamp)
