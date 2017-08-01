import util.util as util


class Song:

    def __init__(self, track_json):

        self.local_timestamp = util.timestamp_to_local(track_json["played_at"])
        self.unix_timestamp = util.timestamp_to_unix(track_json["played_at"])

        track = track_json["track"]
        self.name = track["name"]
        self.popularity = track["popularity"]
        self.duration = track["duration_ms"]
        self.artists = track["artists"]
        self.album = track["album"]
        self.song_id = track["id"]
        self.song_uri = track["uri"]

        self.id = self.song_id + self.local_timestamp.strftime("%H%M%S%d%m%Y")

    def __repr__(self):
        return str.format("{}|{}|{}|", self.id, self.name, self.local_timestamp.strftime("%H:%M:%S %d-%m-%Y"))
