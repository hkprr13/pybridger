#-------------------------------------------------------------------------------
from ...common  import public
from ...utils   import Log
#-------------------------------------------------------------------------------
class SqlEngine:
    """
    Define SQL engine
    """
    def __init__(self) -> None:
        super().__init__()
        self.isLog : bool       = False
        self.log   : Log | None = None
    #---------------------------------------------------------------------------
    @public
    def connect(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def cursor(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def execute(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def executeAny(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def commit(self) -> None: 
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def transaction(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def rollback(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def fetchall(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def isConnected(self) -> None:
        """Implement in the inheritance destination"""
    #---------------------------------------------------------------------------
    @public
    def setLog(self, logFile : str | None) -> None:
        """
        Setting Log class and log flag
        Args:
            logFile (str | None) : log file 
        """
        if logFile is None:
            self.isLog = False
            self.log   = None
        elif logFile:
            self.isLog = True
            self.log   = Log(logFile)
        else:
            self.isLog = False
            self.log   = None
    #---------------------------------------------------------------------------
    @public
    def logDebug(self, msg) -> None:
        """
        Write debug messages to the log
        Args:
            msg (str) : message
        """
        if self.isLog and self.log is not None:
            self.log.debug(msg)
    #---------------------------------------------------------------------------
    @public
    def logInfo(self, msg) -> None:
        """
        Write info messages to the log
        Args:
            msg (str) : message
        """
        if self.isLog and self.log is not None:
            self.log.info(msg)
    #---------------------------------------------------------------------------
    @public
    def logWarning(self, msg) -> None:
        """
        Write warning messages to the log
        Args:
            msg (str) : message
        """
        if self.isLog and self.log is not None:
            self.log.warning(msg)
    #---------------------------------------------------------------------------
    @public
    def logError(self, msg) -> None:
        """
        Write error messages to the log
        Args:
            msg (str) : message
        """
        if self.isLog and self.log is not None:
            self.log.error(msg)
    #---------------------------------------------------------------------------
    @public
    def logCritical(self, msg) -> None:
        """
        Write critical messages to the log
        Args:
            msg (str) : message
        """
        if self.isLog and self.log is not None:
            self.log.critical(msg)   
#-------------------------------------------------------------------------------