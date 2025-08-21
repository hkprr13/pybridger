#-------------------------------------------------------------------------------
from typing         import Any
from .SqlEngine     import SqlEngine
from ...common      import override
from ...common      import public
from ...common      import private
from ...mapper      import Query
#-------------------------------------------------------------------------------
class MySqlEngine(SqlEngine):
    """
    Defined MySQL engine class
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            hostName     : str,
            userName     : str,
            password     : str,
            databaseName : str,
            logFile      : str | None = None
        ):
        """
        Initalize MySQL engine class
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
        except Exception as e:
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
        データベースの接続
        Returns:
            Any : コネクトオブジェクトを返す
        Raises:
            ProgrammingError : 認証エラーやデータベース指定ミス
            InterfaceError   : ソケットエラーやネットワークの接続エラー
            Error            : その他のMySQLエラー
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
                self.logInfo("接続が切れています。再接続を試みます...")
                # Try reconnecting.
                self.conn = self.sqlEngine.connect(
                    host     = self.hostName,
                    user     = self.userName,
                    password = self.password,
                    database = self.databaseName
                )
                return self.conn
            # 再接続に失敗した場合
            except Exception as e:
                msg = "MySQLの再接続に失敗しました"
                # ログ
                self.logError(msg)
                print(f"{msg}: {e}")
                raise Exception
        # 認証エラーやデータベース指定ミスの場合
        except self.sqlEngine.errors.ProgrammingError as pe:
            msg = "認証エラーやデータベース指定ミスです"
            self.logError(msg)
            raise Exception(f"{msg}: {pe}")
        # ネットワークの接続やソケットエラーの場合
        except self.sqlEngine.errors.InterfaceError as ie:
            msg = "ソケットエラーやネットワークの接続エラーです"
            self.logError(msg)
            raise Exception(f"{msg}: {ie}")
        except self.sqlEngine.errors.Error as e:
            # ユーザ名またはパスワードが違う場合
            if e.errno == 1045:
                msg = "ユーザ名またはパスワードが間違っています"
                self.logError(msg)
                raise Exception(msg)
            # 指定されたデータベースが存在しない場合
            elif e.errno == 1049:
                msg = "指定されたデータベースが存在しません"
                self.logError(msg)
                raise Exception(msg)
            # その他
            else:
                msg = f"MySQLエラー({e.errno})です"
                self.logError(msg)
                raise Exception(f"{msg}: {e.msg}")
    #---------------------------------------------------------------------------
    @override
    @public
    def cursor(
            self,
            dictionary : bool = False
        ) -> Any:
        """
        カーソルの作成
        Args:
            dictionary (bool) : 辞書型の指定
        Returns:
            Any : カーソルオブジェクトを返す
        Raises:
            Exception : カーソルの失敗した場合
        """
        try:
            # 接続されていなければ
            if self.conn is None or not self.conn.is_connected():
                self.connect()
            assert self.conn is not None # 明示する
            if self.cur:
                try:
                    self.cur.close()
                except Exception:
                    pass # カーソルが閉じ済みの時用
            self.cur = self.conn.cursor(dictionary = dictionary)
            return self.cur
        except Exception as e:
            msg = "カーソルの作成に失敗しました"
            self.logError(msg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def execute(self, query: Query, value : tuple = ()) -> None:
        """
        クエリの実行
        Args:
            query (Query)   : SQL文
            value (tuple)   : プレイスホルダーに渡す値
        Raises:
            Exception : クエリの実行に失敗した場合
        """
        try:
            self.logDebug(f"クエリ:{query.sql}, 値:{value}")
            self.cursor().execute(query.sql, value)
        except Exception as e:
            msg  = "クエリの実行に失敗しました"
            qmsg = f"クエリ:{query}, 値:{value}"
            self.logError(msg)
            self.logError(qmsg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def executeAny(self, query : Query, data : list[tuple[str]]) -> None:
        """
        クエリの実行(複数)
        Args:
            query (Query)            : クエリ文
            data  (list[tuple[str]]) : プレイスホルダーに渡す値
        Raises:
            Exception : クエリの実行に失敗した場合
        """
        try:
            self.logDebug(f"クエリ:{query.sql}, 値:{data}")
            self.cursor().executemany(query.sql, data)
        except Exception as e:
            msg  = "クエリの実行に失敗しました"
            qmsg = f"クエリ:{query}, 値:{data}"
            self.logError(msg)
            self.logError(qmsg)
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def commit(self) -> None:
        """
        データベースにコミットする
        Raises:
            Exception : コミットに失敗した場合
        """
        try:
            if self.conn and self.conn.is_connected():
                self.conn.commit()
        except Exception as e:
            # コミットが失敗した場合ロールバックする
            msg = "コミットが失敗したためロールバックしました"
            self.logError(msg)
            self.rollback()
            raise Exception(f"{msg}: {e}")
    #---------------------------------------------------------------------------
    @override
    @public
    def transaction(self) -> None:
        """
        トランザクション
        Raises:
            Exception : トランザクションに失敗した場合
        """
        try:
            if self.conn and self.conn.is_connected():
                self.cursor().execute("START TRANSACTION")
        except Exception as e:
            msg = "トランザクションに失敗しました"
            self.logError(msg)
            raise Exception(f"{msg}: {e}") 
    #---------------------------------------------------------------------------
    @override
    @public
    def rollback(self) -> None:
        """
        ロールバック
        Raises:
            Exception : ロールバックに失敗した場合
        """
        try:
            if self.conn and self.conn.is_connected():
                self.conn.rollback()
        except Exception as e:
            msg = "ロールバックに失敗しました"
            self.logError(msg)
            raise Exception(f"{msg}: {e}") 
    #---------------------------------------------------------------------------
    @override
    @public
    def fetchall(self):
        if not self.cur is None:
            return self.cur.fetchall()
    #---------------------------------------------------------------------------
    @override
    @public
    def isConnected(self) -> bool:
        """
        MySQLに接続中かどうか返す
        Returns:
            bool : 接続されていればTrue
        """
        return self.conn is not None and self.conn.is_connected()
#-------------------------------------------------------------------------------