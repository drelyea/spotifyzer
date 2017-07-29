import json


def print_songs(list_of_songs):
    for i in range(len(list_of_songs)):
        print(str.format("{}", list_of_songs[i]))
    print("\n")


def json_to_string(json_result):
    return json.dumps(json_result, sort_keys=True, indent=4)
