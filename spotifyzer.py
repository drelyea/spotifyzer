import sys
import time
import custom_spotipy.util as spotipy_util
import service.service as service

scope = "user-read-recently-played"


def main():

    # setup
    validate_command_args()
    username = sys.argv[1]
    filename = sys.argv[2]

    # log
    print(str.format("Starting Spotifyzer for user {}\nPrinting to file {}\n", username, filename))

    # set default timestamp
    last_unix_timestamp = None

    # continuously query for new songs
    while True:

        # get authentication token
        token = spotipy_util.prompt_for_user_token(username, scope)

        # query
        last_unix_timestamp = service.get_recent_songs(token, 50, last_unix_timestamp, filename)

        # sleep for 1 minute
        # guaranteed to not miss songs with this time
        # over 25 minutes would allow missing songs if skipped at 30 second mark every time
        time.sleep(60)


# checks command args
def validate_command_args():

    # check number of arguments
    if len(sys.argv) != 3:
        print("Error with system arguments. "
              "Expected use: spotifyzer <username> <filename>")
        exit(-1)


if __name__ == '__main__':
    main()
