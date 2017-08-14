import time
import threading
import custom_spotipy.util as spotipy_util
import service.service as service
scope = "user-read-recently-played"


class BackendThread(threading.Thread):
    def __init__(self, threadID, name, username, filename):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.username = username
        self.filename = filename

    def run(self):
        print("Starting {}".format(self.name))
        start_recording_loop(self.username, self.filename)


def start_recording_loop(username, filename):

    # set default timestamp
    last_unix_timestamp = None

    # continuously query for new songs
    while True:

        # get authentication token
        token = spotipy_util.prompt_for_user_token(username, scope)

        # query
        last_unix_timestamp = service.get_recent_songs(token, 50, last_unix_timestamp, filename)

        # sleep for 20 minute
        # guaranteed to not miss songs with this time
        # over 25 minutes would allow missing songs if skipped at 30 second mark every time
        time.sleep(1200)
