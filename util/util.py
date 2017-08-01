import json
import time
from datetime import datetime, timedelta
from dateutil import tz


# prints songs to console
def print_songs(list_of_songs):
    for song in list_of_songs:
        print(str.format("{}\n", song))


# prints songs to file
def print_songs_to_file(list_of_songs, filename):
    file = open(filename, mode="a")
    for song in list_of_songs:
        file.write(str.format("{}\n", song))
    file.close()


# converts a json object to a string
def json_to_string(json_result):
    return json.dumps(json_result, sort_keys=True, indent=4)


# converts spotify timestamp to usable unix millisecond timestamp
def timestamp_to_unix(regular_timestamp):

    date_time_object = datetime.strptime(regular_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    date_time_object = date_time_object - timedelta(hours=5) + timedelta(minutes=1)
    unix_timestamp = time.mktime(date_time_object.timetuple()) * 1000
    int_unix = int(unix_timestamp)

    return int_unix


# converts spotify timestamp to local timezone datetime
def timestamp_to_local(regular_timestamp):

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    date_time_object = datetime.strptime(regular_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    date_time_object = date_time_object.replace(tzinfo=from_zone)
    date_time_object = date_time_object.astimezone(to_zone)
    date_time_object = date_time_object + timedelta(minutes=1)

    return date_time_object
