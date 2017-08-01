import json
import time
import datetime


def print_songs(set_of_songs):
    for song in set_of_songs:
        print(str.format("{}", song))
    print("\n")


def print_songs_to_file(list_of_songs, filename):
    file = open(filename, mode="a")
    for i in range(len(list_of_songs)):
        file.write(str.format("{}", list_of_songs[i]))


def json_to_string(json_result):
    return json.dumps(json_result, sort_keys=True, indent=4)


def timestamp_to_unix(regular_timestamp):
    year, month, day = str.split(regular_timestamp, "-")
    day, rest = str.split(day, "T")
    hour, minute, second = str.split(rest, ":")
    second, millisecond = str.split(second, ".")
    millisecond = millisecond[:-1]

    date_time_object = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(millisecond))
    unix_timestamp = time.mktime(date_time_object.timetuple()) * 1000
    int_unix = int(unix_timestamp)

    print(str.format("\nOld: {}\nDatetime: {}\nNew: {}", regular_timestamp, date_time_object, int_unix))

    return int_unix
