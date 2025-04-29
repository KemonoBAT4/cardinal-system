
import logging

from datetime import datetime

# Log Class, Should be called only by Cardinal
class CardinalLogger():
    """
    Cardinal Logger class
    """

    _logger = None

    # FIXME: fix this class
    def __init__(self):

        self._cleanLog() # cleans the log file

        logging.basicConfig(filename='cardinal.log', encoding='utf-8', level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)
        # pass
    #enddef

    def debug(self, message = "", no_date = False):
        """
        displays a message on the console and on the log file
        """

        full_message = ""
        if no_date:
            full_message = (datetime.now() + ": " + message) # datetime + message, should be used for all the other messages
        else:
            full_message = (message) # only the message, should be used only by cardinal messages

        self._printOnConsole(full_message) # print the message on the console
    #enddef

    def console(self, message = "", no_date = False):
        """
        displays a message on the console and on the log file
        """

        full_message = ""
        if no_date:
            full_message = (f" - {datetime.now()} : {message}") # datetime + message, should be used for all the other messages
        else:
            full_message = (message) # only the message, should be used only by cardinal messages

        self._printOnConsole(full_message) # print the message on the console
    #enddef

    def info(self, message = ""):
        self._logger.info(datetime.now() + ": " + message)

    def warning(self, message = ""):
        """
        displays a warning message on the console and on the log file
        """

        pass
        # self.logger.warning(datetime.now() + ": " + message)
    #enddef

    def error(self, message = ""):
        """
        displays a error message on the console and on the log file
        """
        pass
        # self.logger.error(datetime.now() + ": " + message)
    #enddef

    #############
    # UTILITIES #
    #region #####

    def _cleanLog(self):
        """
        cleans the log file
        """
        # TODO: complete this function
        pass
    #enddef

    def _printOnConsole(self, message):
        print(f'        {message}')
    #enddef

    #endregion -#
#endclass