
import threading
import time

class CardinalThread():
    thread_id = 0
    thread_description = ""
    thread = threading.Thread(target=thread_function, args=(1,))
    def __init__(self, id, description):
        self.thread_id = id
        self.thread_description = description
        # thread = threading.Thread(target=thread_function, args=(1,))

    def start(self):
        return  self.thread.start()

    def join(self):
        return self.thread.join()

