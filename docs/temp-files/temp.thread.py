import threading
import subprocess
import time

class CardinalThread():

    _thread = None
    _thread_id = 0
    _thread_description = ""
    _thread = threading.Thread()
    _thread_status = "not running"

    _classname = "CardinalThread"

    # TODO: fix this class

    def __init__(self):
        pass
    #enddef

    def new(self, id, description, function, args):
        self._thread_id = id
        self._thread_description = description

        # TODO: check if the following lines are working
        if function == 0:
            # run the script passed as argument
            self._thread = threading.Thread(target=self._run_script, args=args)
            return self

        elif function == 1:
            # run the function
            # return threading.Thread(target=function, args=)
            return self
        else:
            return self
    #enddef

    def start(self):
        self.thread_status = "running"
        return  self._thread.start()
    #enddef

    def join(self):
        self.thread_status = "not running"
        return self.thread.join()
    #enddef

    def get_thread_data(self):
        return {
            "thread_id": self._thread_id,
            "thread_description": self._thread_description,
            "thread_status": self._thread_status
        }
    #enddef

    def get_thread_status(self):
        return self._thread_status

    def get_thread(self):
        return self._thread
    #enddef

    #############
    # UTILITIES #
    #############

    def _run_script(self, script_name):
        subprocess.run(["python", script_name])
    #enddef
