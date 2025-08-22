#-------------------------------------------------------------------------------
from typing         import Any
from .SqlEngine     import SqlEngine
from ...common      import override
from ...common      import public
from ...common      import private
from ...utils       import Log
from ...mapper      import Query
#-------------------------------------------------------------------------------
class AsyncPostgreSqlEngine(SqlEngine):
    """

    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            hostName     : str,
            userName     : str,
            password     : str,
            databaseName : str,
            port         : int,
            logFile      : str | None = None
        ):
        """
        PostgreSQLエンジンの初期化
        Args:
            hostName     (str)        : ホスト名
            userName     (str)        : ユーザー名
            password     (str)        : パスワード
            databaseName (str)        : データベース名
            port         (str)        : ポート番号
            logFile      (str | None) : ログファイル名
        """
        super().__init__()
        # インスタンス変数
        self.hostName     = hostName
        self.userName     = userName
        self.password     = password
        self.databaseName = databaseName
        self.port         = port
        try:
            # Check if psycopg is installed
            import psycopg
            self.sqlEngine  = psycopg
        except Exception as e:
            # Check if synchronization psycopg is installed
            raise Exception(
                "psycopg is not installed\n"
                "Please execute the following in Terminal\n"
                "pip install psycopg[binary]"
            )
        try:
            # Check if asynchronous psycopg is installed
            from psycopg import AsyncConnection, AsyncCursor
        except Exception as e:
            raise Exception(
                "asynchronous psycopg is not installed\n"
                "Please execute the following in Terminal\n"
                "pip install psycopg[async]"
            )
        self.conn : AsyncConnection | None = None
        self.cur  : AsyncCursor     | None = None
        self.setLog(logFile)
    #---------------------------------------------------------------------------
    @override
    @public
    async def connect(self) -> Any:
        """
        Connect to database
        Returns:
            Any : Returns connect objct
        Raises:
            Exception : If the database connection fails
        """
        try:
            self.conn = await self.sqlEngine.AsyncConnection.connect(
                host     = self.hostName,
                user     = self.userName,
                password = self.password,
                database = self.databaseName,
                port     = self.port
            )
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
            assert self.conn is not None
            if self.cur:
                try:
                   await self.cur.close()
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
    async def execute(self, query : Query, value: tuple = ()) -> None:
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
            # The return value is set after waiting 
            # for the completion of the connection object's coroutine
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
    async def executeAny(self, query : Query, data: list[tuple[str]]) -> None:
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
            # The return value is set after waiting 
            # for the completion of the connection object's coroutine
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
            if self.conn:
                await self.execute(Query("BEGIN"))
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
        Returns whether or not connected to PostgreSQL
        Returns:
            bool : True if connected
        """
        return self.conn is not None
#-------------------------------------------------------------------------------