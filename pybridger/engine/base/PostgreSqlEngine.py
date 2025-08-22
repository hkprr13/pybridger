#-------------------------------------------------------------------------------
from typing         import Any
from .SqlEngine     import SqlEngine
from ...common      import override
from ...common      import public
from ...common      import private
from ...utils       import Log
from ...mapper      import Query
#-------------------------------------------------------------------------------
class PostgreSqlEngine(SqlEngine):
    """
    Defined PostgreSQL engine class
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
        ) -> None:
        """
        Initalize PostgreSQL engine class
        Args:
            logFile      (str | None) : ログファイル名
            hostName     (str)        : host
            userName     (str)        : user name
            password     (str)        : password
            databaseName (str)        : database
            port         (str)        : ポート番号
            logFile      (str | None) : Specify to obtain the log file.
        """
        super().__init__()
        # インスタンス変数
        self.hostName     = hostName
        self.userName     = userName
        self.password     = password
        self.databaseName = databaseName
        self.port         = port
        # インスタンス変数,(オブジェクト)
        # インスタンスされたタイミングでインポートを行う
        try:
            import psycopg
            self.sqlEngine  = psycopg
        except Exception:
            raise Exception(
                "psycopg is not installed\n"
                "Please execute the following in Terminal\n"
                "pip install psycopg[binary]"
            )
        # コネクトオブジェクトとカーソルオブジェクトの初期化
        self.conn = None
        self.cur  = None
        # ログの初期設定
        self.setLog(logFile)
   #---------------------------------------------------------------------------
    @override
    @public
    def connect(self) -> Any:
        """
        Connect to database
        Returns:
            sqlite3.Connection : Returns connect objct
        Raises:
            Exception : If the database connection fails
        Raises:

        """
        try:
            self.conn = self.sqlEngine.connect(
                host     = self.hostName,
                user     = self.userName,
                password = self.password,
                database = self.databaseName,
                port     = self.port
            )
            return self.conn
        except Exception as e:
            msg = "データベースの接続に失敗しました"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
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
    def execute(self, query: Query, value: tuple = ()) -> None:
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