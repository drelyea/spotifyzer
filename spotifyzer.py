import sys
import time

import util.util as util
import models.song as song
import service.client as spotipy_client
import service.util as spotipy_util

scope = "user-read-recently-played"
set_of_songs = set()


def main():

    validate_command_args()
    username = sys.argv[1]

    token = spotipy_util.prompt_for_user_token(username, scope)

    if token:
        while True:
            get_recent_songs(token, 10)


def get_recent_songs(token, num_songs):
    sp = spotipy_client.Spotify(auth=token)
    json_response = sp.current_user_recently_played(limit=num_songs)
    extract_recent_songs(json_response, num_songs)
    time.sleep(600)


def extract_recent_songs(json_result, num_songs):

    items = json_result["items"]
    for i in range(num_songs):
        data = items[i]
        track = data["track"]
        new_song = song.Song(track["name"], track["artists"][0]["name"], data["played_at"], track["id"])
        set_of_songs.add(new_song)

    util.print_songs(list(set_of_songs))
    print("\n")


def validate_command_args():

    # check number of arguments
    if len(sys.argv) != 2:
        print("Error with system arguments. "
              "Expected use: spotifyzer <username>")
        exit(-1)

if __name__ == '__main__':
    main()
