import util.util as util
import models.song as song
import custom_spotipy.client as spotipy_client

list_of_songs = []


# takes in a spotify token, the number of songs to query, and a timestamp to look after
# queries spotipy api and calls extract_recent_songs
def get_recent_songs(token, num_songs, last_timestamp, filename):

    # get client with token
    sp = spotipy_client.Spotify(auth=token)

    # query spotify
    json_response = sp.current_user_recently_played(limit=num_songs, after=last_timestamp)

    # extract songs and save new query parameter
    last_timestamp = extract_recent_songs(json_response, last_timestamp, filename)

    return last_timestamp


# takes in a json string result and the last recorded timestamp
# extracts each song object and saves it
def extract_recent_songs(json_result, last_timestamp, filename):

    # parse json
    items = json_result["items"]
    songs_available = len(items)

    # only do work if new songs
    if songs_available != 0:
        for i in range(songs_available):

            # parse individual song
            data = items[len(items) - 1 - i]

            # create new song object
            new_song = song.Song(data)

            # save last_timestamp
            last_timestamp = new_song.unix_timestamp

            # add song to list
            list_of_songs.append(new_song)

    # print current set to file
    util.print_songs_to_file(list_of_songs, filename)

    # log
    print(str.format("Added {} songs to {}", len(list_of_songs), filename))

    # clear list
    list_of_songs.clear()

    return last_timestamp
