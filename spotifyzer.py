import sys
import client
import util
import json

scope = "user-read-recently-played"


def main():

    validate_command_args()
    username = sys.argv[1]

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = client.Spotify(auth=token)
        response = sp.current_user()
        print_json(response)


def print_json(json_result):
    print(json.dumps(json_result, sort_keys=True, indent=4))


def validate_command_args():

    # check number of arguments
    if len(sys.argv) != 2:
        print("Error with system arguments. "
              "Expected use: spotifyzer <username>")
        exit(-1)

if __name__ == '__main__':
    main()
