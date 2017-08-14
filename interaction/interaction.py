import threading


class InteractionThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting {}".format(self.name))
        start_interaction()


def start_interaction():

    user_choice = input("Choose an option:\n1:Display All Songs\n")
    print("Do the thing")
