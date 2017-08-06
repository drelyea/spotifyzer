import sys
import asyncio
import backend.backend as backend
import interaction.interaction as interaction


def main():

    # setup
    validate_command_args()
    username = sys.argv[1]
    filename = sys.argv[2]

    # log
    print(str.format("Starting Spotifyzer for user {}\nPrinting to file {}\n", username, filename))

    loop = asyncio.get_event_loop()
    tasks = [backend.start_recording_loop(username, filename), interaction.start_interaction()]
    loop.run_until_complete(asyncio.gather(tasks))
    loop.close()


# checks command args
def validate_command_args():

    # check number of arguments
    if len(sys.argv) != 3:
        print("Error with system arguments. "
              "Expected use: spotifyzer <username> <filename>")
        exit(-1)


if __name__ == '__main__':
    main()
