import sys
import time
import custom_spotipy.util as spotipy_util
import service.service as service

scope = "user-read-recently-played"


def main():

    validate_command_args()
    username = sys.argv[1]

    # get authentication token
    token = spotipy_util.prompt_for_user_token(username, scope)

    last_unix_timestamp = None

    if token:
        # continuously query for new songs
        while True:
            last_unix_timestamp = service.get_recent_songs(token, 10, last_unix_timestamp)
            print(str.format("\nLast Timestamp: {}", last_unix_timestamp))
            time.sleep(1200)


def validate_command_args():

    # check number of arguments
    if len(sys.argv) != 2:
        print("Error with system arguments. "
              "Expected use: spotifyzer <username>")
        exit(-1)


if __name__ == '__main__':
    main()
