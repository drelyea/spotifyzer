import sys
import client
import util
import json
import time

scope = "user-read-recently-played"
list_of_songs = set()


def main():

    validate_command_args()
    username = sys.argv[1]

    token = util.prompt_for_user_token(username, scope)

    if token:
        while True:
            get_recent_songs(token, 10)


def get_recent_songs(token, num_songs):
    sp = client.Spotify(auth=token)
    json_response = sp.current_user_recently_played(limit=num_songs)
    extract_recent_songs(json_response, num_songs)

    time.sleep(600)


def extract_recent_songs(json_result, num_songs):

    items = json_result["items"]
    for i in range(num_songs):
        song = items[i]
        track = song["track"]
        name = track["name"]
        list_of_songs.add(name)

        print(list_of_songs)

    print("\n")

def json_to_string(json_result):
    return json.dumps(json_result, sort_keys=True, indent=4)


def validate_command_args():

    # check number of arguments
    if len(sys.argv) != 2:
        print("Error with system arguments. "
              "Expected use: spotifyzer <username>")
        exit(-1)

if __name__ == '__main__':
    main()
