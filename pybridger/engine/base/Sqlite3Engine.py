#-------------------------------------------------------------------------------
import sqlite3
from typing         import Any
from .SqlEngine     import SqlEngine
from ...common      import override
from ...common      import public
from ...mapper      import Query
#-------------------------------------------------------------------------------
class Sqlite3Engine(SqlEngine):
    """
    Defined Sqlite3 engine class
    """
    PLACEHOLDER : str = "?"
    #---------------------------------------------------------------------------
    def __init__(
            self,
            databasePath : str,
            logFile      : str | None = None
        ) -> None:
        """
        Initialize Sqlite3 engine class
        Args:
            databasePath (str)        : database path
            logFile      (str | None) : lof file
        """
        super().__init__()
        self.database : str = databasePath
        self.sqlEngine = sqlite3
        self.conn : sqlite3.Connection | None = None
        self.cur  : sqlite3.Cursor     | None = None
        self.setLog(logFile)
    #---------------------------------------------------------------------------
    @override
    @public
    def connect(self) -> sqlite3.Connection:
        """
        Connect to database
        Returns:
            sqlite3.Connection : Returns connect object
        Raises:
            Exception : If the database connection fails
        """
        try:
            self.conn = self.sqlEngine.connect(self.database)
            return self.conn
        except sqlite3.IntegrityError as e:
            msg = "Constraint violation (UNIQUE/NOT NULL/FOREIGN KEY/CHECK)"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
        except sqlite3.OperationalError as e:
            msg = "Errors such as lock/syntax/non-existent table/file/I/O, etc"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
        except sqlite3.ProgrammingError as e:
            msg = "These are errors such as API misuse, binding mismatch," \
                  "post-close operations, and thread misuse."
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
        except sqlite3.InterfaceError as e:
            msg = "This is an error such as an unhandled bind"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
        except sqlite3.DatabaseError as e:
            msg = "Errors such as damage or incorrect format"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")              
    #---------------------------------------------------------------------------
    @override
    @public
    def cursor(self) -> sqlite3.Cursor:
        """
        Creating cursor object
        Returns:
            Any : Returns the cursor object
        Raises:
            Exception : If the cursor fails
        """
        try:
            if self.conn is None:
                self.connect()
            assert self.conn is not None
            self.cur = self.conn.cursor()
            return self.cur
        except Exception as e:
            msg = "Failed to create cursor"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------    
    @override
    @public
    def execute(self, query : Query, value : tuple = ()) -> None:
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
    def executeAny(self, query : Query, data: list[tuple[str]]) -> None:
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
            if self.conn:
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
            if self.conn:
                self.cursor().execute("BEGIN")
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
            if self.conn:
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
        return self.conn is not None
#-------------------------------------------------------------------------------