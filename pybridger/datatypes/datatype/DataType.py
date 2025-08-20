#-------------------------------------------------------------------------------
from typing         import Any
from ...error       import EngineUndefinedError #
from ...error       import EngineSetupError     #
from ...error       import PyBridgerError       #
from ...common      import private              #
from ...common      import public               #
from ...config      import Config               # コンフィグクラス
from ...query       import Query
#-------------------------------------------------------------------------------
class DataType:
    TEXTNOTSUPPORTED: str = "Not supported"
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        self.query : Any
    #---------------------------------------------------------------------------
    @public
    def checkSettingEngine(self):
        # 同期エンジンと非同期エンジンが未設定なら
        if Config.sqlEngine is None and Config.asyncSqlEngine is None:
            raise EngineUndefinedError()
        # 同期エンジンが設定かつ、非同期エンジンが未設定
        elif Config.asyncSqlEngine is None and Config.sqlEngine is not None:
            self.sqlEngine = Config.sqlEngine
        # 同期エンジンが未設定かつ、非同期エンジンが設定されている
        elif Config.sqlEngine is None and Config.asyncSqlEngine is not None:
            self.sqlEngine = Config.asyncSqlEngine
        else:
            raise EngineSetupError()
    #---------------------------------------------------------------------------
    @public
    def mysql(self) -> None: ...
    #---------------------------------------------------------------------------
    @public
    def sqlite3(self) -> None: ...
    #---------------------------------------------------------------------------
    @public
    def postgresql(self) -> None: ...
    #---------------------------------------------------------------------------
    @public
    def toQuery(self) -> Any:
        self.checkSettingEngine()
        if self.sqlEngine == Config.mySqlEngine:
            self.mysql()
        elif self.sqlEngine == Config.sqlite3Engine:
            self.sqlite3()
        elif self.sqlEngine == Config.postgreSqlEngine:
            self.postgresql()
        else:
            raise EngineUndefinedError()
        return self.query
#-------------------------------------------------------------------------------