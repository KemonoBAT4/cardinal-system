
import threading
import subprocess

import time

class CardinalThread():

    def _run_script(script_name):        
        subprocess.run(["python", script_name]) 

    thread_id = 0
    thread_description = ""
    thread = threading.Thread()
    thread_status = "not running"

    def __init__(self, id, description, function, args):
        
        self.thread_id = id
        self.thread_description = description

        if function == 0:
            thread = threading.Thread(target=self._run_script, args=args)
        elif function == 1:
            pass
        elif function == 2:
            pass
        else:
            # return erros
            pass

    def start(self):
        self.thread_status = "running"
        return  self.thread.start()

    def join(self):
        self.thread_status = "not running"
        return self.thread.join()

