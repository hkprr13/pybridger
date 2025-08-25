#-------------------------------------------------------------------------------
from typing         import Any
from .SqlEngine     import SqlEngine
from ...common      import override
from ...common      import public
from ...common      import private
from ...utils       import Log
from ...mapper      import Query
#-------------------------------------------------------------------------------
class AsyncMySqlEngine(SqlEngine):
    """
    Asynchronous MySQL engine class
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
        Initialize asynchronous engine class
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
        # Display an error message when the driver is not installed
        try:
            import aiomysql
            self.sqlEngine  = aiomysql
        except Exception as e:
            raise Exception(
                "aiomysql is not installed\n"
                "Please execute the following in Terminal\n"
                "pip install aiomysql"
            )
        self.conn = None # Initial value is None
        self.cur  = None # Initial value is None
        self.setLog(logFile) 
    #---------------------------------------------------------------------------
    @override
    @public
    async def connect(self) -> Any:
        """
        Connect to MySQL asynchronously and create a pool
        Returns:
            Any : Returns connect object
        Raises:
            Exception : If the database connection fails
        """
        try:
            self.pool = await self.sqlEngine.create_pool(
                host       = self.hostName,
                user       = self.userName,
                password   = self.password,
                db         = self.databaseName,
                autocommit = False
            )
            self.conn = await self.pool.acquire()
            return self.conn
        except Exception as e:
            msg = "Failed to connect to the database"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    async def cursor(self) -> Any:
        """
        Creating cursor object
        Returns:
            Any : Returns the cursor object
        Raises:
            Exception : If the cursor fails
        """
        try:
            if self.conn is None:
                await self.connect()
            if not self.conn:
                raise Exception
            # The return value is set after waiting 
            # for the completion of the connection object's coroutine
            self.cur  = await self.conn.cursor()
            return self.cur
        except Exception as e:
            msg = "Failed to create cursor"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    async def execute(self, query: Query, value: tuple = ()) -> None: 
        """
        Execute SQL queries asynchronously
        Args:
            query (Query)   : query object
            value (tuple)   : Value passed to placeholder
        Raises:
            Exception : If the query fails
        """
        try:
            qmsg = f"query:{query.sql}, value:{value}"
            self.logDebug(qmsg)
            cur = await self.cursor()
            await cur.execute(query.sql, value)
        except Exception as e:
            msg  = "The query failed"       
            self.logError(msg)
            self.logError(qmsg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------    
    @override
    @public
    async def executeAny(self, query : Query, data : list[tuple[str]]) -> None:
        """
        Execute SQL queries asynchronously(multiple)
        Args:
            query (Query)            : query object
            data  (list[tuple[str]]) : Value passed to placeholder
        Raises:
            Exception : If the query fails
        """
        try:
            qmsg = f"query:{query.sql}, value:{data}"
            cur = await self.cursor()
            await cur.executemany(query.sql, data)
        except Exception as e:
            msg  = "The query failed"       
            self.logError(msg)
            self.logError(qmsg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    async def commit(self) -> None:
        """
        Commit the transaction
        Raises:
            Exception : If the commit fails
        """
        try:
            if self.conn:
                await self.conn.commit()
        except Exception as e:
            msg = "Rollback performed due to failed commit"
            self.logError(msg)
            await self.rollback()
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    async def transaction(self) -> None:
        """
        Transaction asynchronously
        Raises:
            Exception : If the transaction fails
        """
        try:
            await self.cursor()
            await self.execute(Query("START TRANSACTION"))
        except Exception as e:
            msg = "Transaction failed"
            self.logError(msg)
            raise Exception(f"{msg}: {e}") 
    #---------------------------------------------------------------------------
    @override
    @public
    async def rollback(self) -> None:
        """
        Rollback asynchronously
        Raises:
            Exception : If the rollback fails
        """
        try:
            if self.conn:
                await self.conn.rollback()
        except Exception as e:
            msg = "Rollback failed"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
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
