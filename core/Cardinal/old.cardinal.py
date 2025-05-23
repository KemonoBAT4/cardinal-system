
import os
import uuid
import socket
import configparser
import threading
import time
import subprocess

from ..Threads.threadManager import ThreadManager
from ..Logging.cardinalLogger import CardinalLogger

from ..Handler.consoleHandler import ConsoleHandler

class Cardinal:
    # region ---- cardinal variables ---------- #

    # cardinal personal info
    _uid = None # cardinal's unique id
    _classname = "Cardinal"

    _is_running = False # cardinal status
    _host = None # cardinal host
    _port = None # cardinal port
    _max_connections = None # cardinal max connections
    _current_connection = None # cardinal current connection
    _config = None # cardinal config file
    _logger = None # cardinal logger script

    # cardinal master info
    _master = None # Cardinal | none, cardinal master's

    # threads & thread manager
    _threads = []
    _queued_threads = []
    _active_threads = []
    _closed_threads = []

    # cardinal children info
    _childrens = [] # should be a list of cardinals
    _cardinal_childrens_connection = None # cardinl's connection with childrens

    # cardinal applications
    _applications = dict()

    # endregion-- cardinal variables ---------- #

    # init
    def __init__(self, master = None,  *args, **kwargs):

        self._config = configparser.ConfigParser()
        self._config.read("application.cfg")
        self._uid = self._generateUid()

        # setting the logger
        self._logger = CardinalLogger()
        self._consoleHandler = ConsoleHandler()
        

        #region setting the master infos
        if isinstance(master, Cardinal) and master != None:
            self._master = master
            self._logger.console(f"Starting Cardianl With Master {self._master.getCardinalUid()}")
        #endregion master infos
    #enddef

    def _handler(self):
        try:
            # creates the server
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # retrieves the application's host and port
            self._host = str(self._config.get('Cardinal', 'host'))
            self._port = int(self._config.get('Cardinal', 'port'))
            self._max_connections = int(self._config.get('Cardinal', 'max_connections'))

            server.bind((self._host, self._port)) # bind the host and port
            server.listen(self._max_connections) # set the max possible connections at the same time

            self._is_running = True # switch status

            self._logger.debug(self._showStartData()) # show starting data

            self._logger.console("starting the console handler")
            cli_thread = threading.Thread(target=self._consoleHandler.handler) # start the console handler
            cli_thread.start()
            self._logger.console("started the console handler")
            return False

            # cardinal's core handler
            # TODO: complete this function
            while self._is_running != False:
                client_socket, address = server.accept()
                print(f"Connection from {address} has been established.")

                data = client_socket.recv(1024).decode()

                if data:
                    pass
                    # self._handleData(address, data)
                else:
                    self._logger.debug("No data received")
                    self._logger.debug("Closing the connection with the client")
                    client_socket.close()
                #endif

        except Exception as ex:
            # TODO: implement the error logger
            self._logger.error(ex)
            self._logger.debug("Error while starting Cardinal, check the error log for more details")
            return False
        #endtry
    #enddef

    def _handleData(self, address, data):
        pass
    #enddef

    ####################
    # PUBLIC UTILITIES #
    #region ############

    # once initialized starts cardinal
    def start(self):
        self._cardinalStart()
    #enddef

    # shuts down cardinal
    def shutdown(self, rebootchildrens):
        try:
            # this is needed if you want to prevent from shutting down other cardinal's instances
            if rebootchildrens:
                self._shutdownAllChildren() # shuts down all the cardinal sub - instances
            self._is_running = False
            return True # retuns true if action shutdown successfully
        except Exception as ex:
            self._logger.error(ex)
            if self._is_running == True:
                return False
            else:
                return True
    #enddef

    def getCardinalUid(self):
        """
        DESCRIPTION:
        gives the cardinal uid

        PARAMETERS:
         - no parameters required
        
        RETURN:
         - str: the cardinal uid
        """

        return self._uid
    #enddef

    def getCardinalData(self) -> dict:
        """
        DESCRIPTION:
        gives the cardinal core date

        PARAMETERS:
         - no parameters required
        
        RETURN:
         - dict: a dictionary containing all the informations needed
        """
        data = dict()

        # FIXME: check if the infos like master_uid and others are correct
        # probably they are not

        data['id'] = self._uid # cardinals uid
        data['running'] = self._is_running # if the cardinal is running
        data['master_uid'] = self._master_uid # cardinal master's uid
        data['master_connection'] = self._master_connection # cardinal master's connection
        data['threads'] = self._threads # cardinal's threads
        data['childrens'] = self._childrens # cardinal's possible childrens
        data['applications'] = self._applications # cardinal's applications

        return data
    #enddef

    def cardianlReboot(self, rebootchildrens = True):
        """
        DESCRIPTION:
        reboots cardinal and its childrens

        PARAMETERS:
         - rebootchildrens: True if the childrens have to be restarted too, False if you want to restart only cardinal
        
        RETURN:
         - no return
        """

        self.shutdown(rebootchildrens)
        self._cardinalStart() # TODO: complete by adding if the cardinal wants to prevent the reboot of the children
    #enddef

    def isRunning(self) -> bool:
        """
        DESCRIPTION:
        checks the cardinal running status

        PARAMETERS:
         - no parameters required
        
        RETURN:
         - bool: True if cardinal is still running else False 
        """
        return self._is_running
    #enddef
    #endregion ##########

    #####################
    # PRIVATE UTILITIES #
    #####################

    def _consoleHandler(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self._host, self._port)
        client_socket.connect(server_address)
        while self._is_running:

            command = input("Enter command (type 'help' for a list of commands): ")
            query = command.strip().lower()
            if query == 'shutdown' or query == 'shut':
                self._is_running = False
                self._logger.console("Shutting down the server...")
                print("Shutting down the server...")
            else:
                self._logger.debug(f"Received command: {query}")
                # Handle other commands here if needed
        #endwhile

    # starts the whole application
    def _cardinalStart(self):
        try:
            # creates the server
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # retrieves the application's host and port
            self._host = str(self._config.get('Cardinal', 'host'))
            self._port = int(self._config.get('Cardinal', 'port'))
            self._max_connections = int(self._config.get('Cardinal', 'max_connections'))

            server.bind((self._host, self._port)) # bind the host and port
            server.listen(self._max_connections) # set the max possible connections at the same time

            self._is_running = True # switch status

            self._logger.debug(self._showStartData())
            # cardinal's core handler
            while self._is_running != False:
                client_socket, address = server.accept()
                print(f"Connection from {address} has been established.")

        except Exception as ex:
            # TODO: implement the error logger
            self._logger.error(ex)
            self._logger.debug("Error while starting Cardinal, check the error log for more details")
            pass
    #enddef

    def _consoleHandler(self):

        while self._is_running:
            command = input("Enter command (type 'help' for a list of commands): ")
            if command.strip().lower() == 'exit':
                self._is_running = False
                self._logger.debug("Shutting down the console handler...")
                print("Shutting down the console handler...")
            else:
                self._logger.debug(f"Received command: {command}")
                # Handle other commands here if needed
        #endwhile
    #enddef

    def _shutdownAllChildren(self):
        for children in self._childrens:
            try:
                if children.isRunning() == True:
                    response = self._shutdownChild(children)

                    if response == True:
                        self._logger.debug(f"Children {children.getCardinalUid()} has been shutdown")
                    else:
                        self._logger.debug(f"Error while shutting down children {children.getCardinalUid()}")
                    #endif
                else:
                    self._logger.debug(f"Children {children.getCardinalUid()} is not running")
                #endif
            except Exception as ex:
                self._logger.debug(f"Error while shutting down children {children.getCardinalUid()}")
                self._logger.error(ex)
            #endtry
        #endfor
    #enddef

    def _shutdownChild(self, child):
        """
        DESCRIPTION:
        shuts down a cardinal child

        PARAMETERS:
         - child: the child to shutdown
        
        RETURN:
         - True if the child has been shutdown
        """
        return child.shutdown()
    #enddef

    def _showStartData(self) -> str:
        return f"""

        #######################
        # WELCOME TO CARDINAL #
        #######################

        booting now . . .

        # --- CARDINAL INFORMATIONS --- #
        - current Cardinal version: {self._config.get('Cardinal', 'version')}
        - author: {self._config.get('Cardinal', 'author')}
        - source code: {self._config.get('Cardinal', 'source')}

        """
    #enddef

    def _start_cardinal_listener_thread(self):
        clt = ThreadManager.newThread(id = self._generateUid(), description = "Cardinal Listener", function = 0, args="TODO: set function")
        ThreadManager.startThread(clt)
    #enddef

    def _newChildren(self):
        new = Cardinal(master=self)
        self._childrens.append(new)
    #enddef

    def _generateUid(self):
        """
        DESCRIPTION:
        generates a new unique id

        PARAMETERS:
         - no parameters required
        
        RETURN:
         - str: the generated uid
        """
        return str(uuid.uuid4())
    #enddef
#endclass
