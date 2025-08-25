#-------------------------------------------------------------------------------
from .base      import MySqlEngine     
from .base      import Sqlite3Engine  
from .base      import PostgreSqlEngine 
from ..common   import public 
from ..schema   import Column
from ..model    import Model
from ..manager  import Select 
from ..config   import Config
#-------------------------------------------------------------------------------
class Engine:
    """
    SQLエンジンを初期化・管理するためのクラス
    データベースの接続設定、エンジンの初期化、SQL発行に必要な
    各種情報の取得・設定を提供する
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            sqlEngineName : str,
            hostName      : str | None = None,
            userName      : str | None = None,
            password      : str | None = None,
            database      : str | None = None,
            port          : int | None = None,
            logFile       : str | None = None
        ):
        """
        エンジンを初期化し、接続情報を登録する。
        Args:
            sqlEngineName (str) : 使用するエンジン名
            hostName      (str) : ホスト名
            userName      (str) : ユーザー名
            password      (str) : パスワード
            databaseName  (str) : データベース名またはDBファイルパス
        """
        self.sqlEngineName = sqlEngineName 
        self.hostName      = hostName
        self.userName      = userName
        self.password      = password
        self.database      = database
        self.port          = port
        self.logFile       = logFile
    #---------------------------------------------------------------------------
    @public
    def launch(self) -> None:
        """
        SQLエンジンをエンジン名に応じて初期化する
        Raises:
            ModuleNotFoundError : 未対応のエンジン名が指定された場合
        """
        if self.sqlEngineName.lower() == "sqlite3":
            if self.database:
                self.sqlEngine = Sqlite3Engine(
                    databasePath = self.database,
                    logFile      = self.logFile
                )
            else:
                raise Exception("データベースを指定してください")
        elif self.sqlEngineName.lower() == "mysql":
            if  self.hostName and self.userName \
            and self.password and self.database:
                self.sqlEngine = MySqlEngine(
                    hostName     = self.hostName,
                    userName     = self.userName,
                    password     = self.password,
                    databaseName = self.database,
                    logFile      = self.logFile
                )
            else:
                raise Exception("引数を指定ください")
        elif self.sqlEngineName.lower() == "postgresql":
            if  self.hostName and self.userName \
            and self.password and self.database \
            and self.port:
                self.sqlEngine = PostgreSqlEngine(
                    hostName     = self.hostName,
                    userName     = self.userName,
                    password     = self.password,
                    databaseName = self.database,
                    port         = self.port,
                    logFile      = self.logFile
                )
            else:
                raise Exception("引数を指定ください")
        else:
            raise ModuleNotFoundError("未対応のモジュールエンジンです")
        Config.sqlEngine = self.sqlEngine
        Config.database  = self.database
    #---------------------------------------------------------------------------
    @public
    def commit(self) -> None:
        """
        トランザクションをコミットする
        """
        self.sqlEngine.commit()
    #---------------------------------------------------------------------------
    @public
    def select(
            self,
            table    : type[Model],
            *columns : Column
        ) -> Select:
        """
        SELECT文用のSelectオブジェクトを生成する
        Args:
            table   (type[Model]) : モデルクラス
            columns (Column...)   : 取得対象のカラム
        Returns:
            Select : SELECTクラス
        """
        return Select(
            tableName  = table.tableName, # テーブル名 
            columns    = columns            # カラム
        )
#-------------------------------------------------------------------------------
