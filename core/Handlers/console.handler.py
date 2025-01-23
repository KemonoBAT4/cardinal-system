
from core.Logging.cardinalLogger import CardinalLogger

class ConsoleHandler:

    _classname = "CardinalConsoleHandler"
    _logger = None

    def __init__(self, logger: CardinalLogger):
        self._logger = logger
    #enddef

    def handler(self, ):




        query = q.strip().lower()

        if query == 'shutdown' or query == 'shut':
            return 

        
    #enddef
#endclass