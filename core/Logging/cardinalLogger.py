
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

        self.clear() # cleans the log file

        # setup logging
        logging.basicConfig(filename='cardinal.log', encoding='utf-8', level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)
    #enddef

    def debug(self, message = "", no_date = False):
        """
        displays a message on the console and on the log file
        """

        full_message = self._buildMessage(message=message, no_date=no_date) # gets the final message to print / others
        self._printOnConsole(full_message) # print the message on the console
    #enddef

    def console(self, message: str = "", no_date: bool = False):
        """
        DESCRIPTION:
        Prints the message only in the console.

        PARAMETERS:
        - message (str): The message to print.
        - no_date (bool): If True, the date will not be printed.

        RETURN:
        - no return
        """

        full_message = self._buildMessage(message=message, no_date=no_date)

        self._printOnConsole(full_message) # print the message on the console
    #enddef

    # TODO: Implement this functions
    # def info(self, message = ""):
    #     self._logger.info(datetime.now() + ": " + message)

    # def warning(self, message = ""):
    #     """
    #     displays a warning message on the console and on the log file
    #     """

    #     pass
    #     # self.logger.warning(datetime.now() + ": " + message)
    # #enddef

    def error(self, message = ""):
        """
        displays a error message on the console and on the log file
        """
        pass
        # self.logger.error(datetime.now() + ": " + message)
    #enddef

    def clear(self) -> dict:
        return self._cleanLog()
    #enddef

    #############
    # UTILITIES #
    #region #####

    def _buildMessage(self, message, no_date = False):
        full_message = ""
        if no_date:
            full_message = (datetime.now() + ": " + message) # datetime + message, should be used for all the other messages
        else:
            full_message = (message) # only the message, should be used only by cardinal messages

        return full_message
    #enddef

    def _cleanLog(self) -> dict:
        """
        cleans the log file
        """

        response = {
            "status": True,
            "message": "Log file cleaned successfully"
        }

        try:
            with open('cardinal.log', 'w', encoding='utf-8'):
                return response
            #endwith
        except Exception as e:
            response["status"] = False
            response["message"] = f'Error: {str(e)}'
            return response
        #endtry
    #enddef

    def _printOnConsole(self, message):
        print(f'        {message}')
    #enddef


    #endregion -#
#endclass