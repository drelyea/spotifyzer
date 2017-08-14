import sys
import backend.backend as backend
import interaction.interaction as interaction


def main():

    # setup
    validate_command_args()
    username = sys.argv[1]
    filename = sys.argv[2]

    # log
    print(str.format("Starting Spotifyzer for user {}\nPrinting to file {}\n", username, filename))

    back = backend.BackendThread(1, "Backend-Thread", username, filename)
    inter = interaction.InteractionThread(1, "Interaction-Thread")
    back.start()
    inter.start()
    back.join()
    inter.join()

    # close
    print("Exiting main thread")


# checks command args
def validate_command_args():

    # check number of arguments
    if len(sys.argv) != 3:
        print("Error with system arguments. "
              "Expected use: spotifyzer <username> <filename>")
        exit(-1)


if __name__ == '__main__':
    main()
