#-------------------------------------------------------------------------------
from multiprocessing import Value
from typing         import Any
from .SqlEngine     import SqlEngine
from ...common      import override
from ...common      import public
from ...mapper      import Query
#-------------------------------------------------------------------------------
class MySqlEngine(SqlEngine):
    """
    Defined MySQL engine class
    """
    PLACEHOLDER : str = "%s"
    #---------------------------------------------------------------------------
    def __init__(
            self,
            hostName     : str,
            userName     : str,
            password     : str,
            databaseName : str,
            logFile      : str | None = None
        ) -> None:
        """
        Initialize MySQL engine class
        Args:
            hostName     (str)        : host
            userName     (str)        : user name
            password     (str)        : password
            databaseName (str)        : database
            logFile      (str | None) : Specify to obtain the log file.
        """
        super().__init__()
        self.hostName     = hostName
        self.userName     = userName
        self.password     = password
        self.databaseName = databaseName
        try:
            import mysql.connector
            self.sqlEngine  = mysql.connector
        except Exception:
            raise Exception(
                "mysql.connnector is not installed\n"
                "Please execute the following in Terminal\n"
                "pip install mysql-connector-python"
            )
        self.conn = None
        self.cur  = None
        self.setLog(logFile)
    #---------------------------------------------------------------------------
    @override
    @public
    def connect(self) -> Any:
        """
        Connect to database
        Returns:
            Any : Returns the connect object
        Raises:
            ProgrammingError : Authentication errors and database specification errors
            InterfaceError   : Socket errors and network connection errors
            Error            : Other MySQL errors
        """
        try:
            self.conn = self.sqlEngine.connect(
                host     = self.hostName,
                user     = self.userName,
                password = self.password,
                database = self.databaseName
            )
            return self.conn
        # If the connection to the database is lost
        except self.sqlEngine.errors.OperationalError as oe:
            try:
                self.logInfo(
                    "The connection has been lost. Attempting to reconnect..."
                )
                # Try reconnecting.
                self.conn = self.sqlEngine.connect(
                    host     = self.hostName,
                    user     = self.userName,
                    password = self.password,
                    database = self.databaseName
                )
                return self.conn
            # If reconnection fails
            except Exception as e:
                msg = "Reconnection failed"
                self.logError(msg)
                raise Exception
        except self.sqlEngine.errors.ProgrammingError as pe:
            msg = "Authentication error or database specification error"
            self.logError(msg)
            raise Exception(f"{msg}: {pe}")
        except self.sqlEngine.errors.InterfaceError as ie:
            msg = "Socket error or network connection error"
            self.logError(msg)
            raise Exception(f"{msg}: {ie}")
        except self.sqlEngine.errors.Error as e:
            if e.errno == 1045:
                msg = "Your username or password is incorrect"
                self.logError(msg)
                raise Exception(msg)
            elif e.errno == 1049:
                msg = "The specified database does not exist"
                self.logError(msg)
                raise Exception(msg)
            # その他
            else:
                msg = f"MySQL error({e.errno}"
                self.logError(msg)
                raise Exception(f"{msg}: {e.msg}")
    #---------------------------------------------------------------------------
    @override
    @public
    def cursor(self) -> Any:
        """
        Creating cursor object
        Returns:
            Any : Returns the cursor object
        Raises:
            Exception : If the cursor fails
        """
        try:
            # If not connected
            if self.conn is None or not self.conn.is_connected():
                self.connect()
            assert self.conn is not None
            if self.cur:
                try:
                    self.cur.close()
                except Exception:
                    pass
            self.cur = self.conn.cursor()
            return self.cur
        except Exception as e:
            msg = "Failed to create cursor"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def execute(self, query: Query, value : tuple = ()) -> None:
        """
        Execute query
        Args:
            query (Query)   : query object
            value (tuple)   : Value passed to placeholder
        Raises:
            Exception : If the query fails
        """
        try:
            qmsg = f"query:{query.sql}, value:{value}"
            self.logDebug(qmsg)
            self.cursor().execute(query.sql, value)
        except Exception as e:
            msg  = "The query failed"       
            self.logError(msg)
            self.logError(qmsg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def executeAny(self, query : Query, data : list[tuple[str]]) -> None:
        """
        Execute query(multiple)
        Args:
            query (Query)            : query object
            data  (list[tuple[str]]) : Value passed to placeholder
        Raises:
            Exception : If the query fails
        """
        try:
            qmsg = f"query:{query.sql}, value:{data}"
            self.logDebug(qmsg)
            self.cursor().executemany(query.sql, data)
        except Exception as e:
            msg  = "The query failed"       
            self.logError(msg)
            self.logError(qmsg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def commit(self) -> None:
        """
        Commit the transaction
        Raises:
            Exception : If the commit fails
        """
        try:
            if self.conn and self.conn.is_connected():
                self.conn.commit()
        except Exception as e:
            msg = "Rollback performed due to failed commit"
            self.logError(msg)
            self.rollback()
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def transaction(self) -> None:
        """
        Transaction
        Raises:
            Exception : If the transaction fails
        """
        try:
            if self.conn and self.conn.is_connected():
                self.cursor().execute("START TRANSACTION")
        except Exception as e:
            msg = "Transaction failed"
            self.logError(msg)
            raise Exception(f"{msg}: {e}") 
    #---------------------------------------------------------------------------
    @override
    @public
    def rollback(self) -> None:
        """
        Rollback
        Raises:
            Exception : If the rollback fails
        """
        try:
            if self.conn and self.conn.is_connected():
                self.conn.rollback()
        except Exception as e:
            msg = "Rollback failed"
            self.logError(msg)
            raise Exception(f"{msg}: {e}") 
    #---------------------------------------------------------------------------
    @override
    @public
    def fetchall(self) -> list[Any] | None:
        """
        Rollback
        Raises:
            Exception : If the rollback fails
        """
        if not self.cur is None:
            return self.cur.fetchall()
    #---------------------------------------------------------------------------
    @override
    @public
    def isConnected(self) -> bool:
        """
        Returns whether or not connected to MySQL
        Returns:
            bool : True if connected
        """
        return self.conn is not None and self.conn.is_connected()
#-------------------------------------------------------------------------------