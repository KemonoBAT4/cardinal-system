
import threading
import time

class CardinalThread():
    thread_id = 0
    thread_description = ""
    thread = threading.Thread()
    thread_status = "not running"

    def __init__(self, id, description, function):
        self.thread_id = id
        self.thread_description = description
        thread = threading.Thread(target=function, args=(1,))

    def start(self):
        self.thread_status = "running"
        return  self.thread.start()

    def join(self):
        self.thread_status = "not running"
        return self.thread.join()

