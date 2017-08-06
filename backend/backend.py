import time
import custom_spotipy.util as spotipy_util
import service.service as service
scope = "user-read-recently-played"


async def start_recording_loop(username, filename):

    # log
    print("Starting Backend Module...")

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
