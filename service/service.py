import time

import util.util as util
import models.song as song
import custom_spotipy.client as spotipy_client

set_of_songs = set()
set_of_ids = set()


def get_recent_songs(token, num_songs, last_timestamp):
    sp = spotipy_client.Spotify(auth=token)
    print(str.format("Trying with timestamp: {}", last_timestamp))
    json_response = sp.current_user_recently_played(limit=num_songs, after=last_timestamp)
    last_timestamp = extract_recent_songs(json_response, last_timestamp)
    return last_timestamp


def extract_recent_songs(json_result, last_timestamp):

    items = json_result["items"]

    songs_available = len(items)

    if songs_available == 0:
        print("\nNo New Songs\n")
    else:
        for i in range(songs_available):
            data = items[len(items) - 1 - i]
            track = data["track"]
            new_song = song.Song(track["name"], track["artists"][0]["name"], data["played_at"], track["id"])

            last_timestamp = util.timestamp_to_unix(new_song.timestamp)

            set_of_songs.add(new_song)
            print(str.format("Got Song: {}\n", new_song.name))

    # util.print_songs(set_of_songs)

    return last_timestamp
