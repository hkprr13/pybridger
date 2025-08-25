#-------------------------------------------------------------------------------
from typing     import Any
from ..config   import Config
from ..common   import private
from ..engine   import Sqlite3Engine
from ..engine   import MySqlEngine
from ..engine   import PostgreSqlEngine
from ..errors   import EngineUndefinedError
#-------------------------------------------------------------------------------
class Session:
    def __init__(self) -> None:
        self.__conn = None
    #---------------------------------------------------------------------------
    @property
    @private
    def __sqlEngine(self) -> Sqlite3Engine | MySqlEngine | PostgreSqlEngine:
        engine = Config.sqlEngine
        if engine is None:
            raise  EngineUndefinedError()
        return engine
    #---------------------------------------------------------------------------
    def __enter__(self) -> Any:
        self.__conn = self.__sqlEngine.connect()
        return self.__conn
    #---------------------------------------------------------------------------
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                if self.__conn:
                    self.__conn.commit()
            else:
                if self.__conn:
                    self.__conn.rollback()
        finally:
            if self.__conn:
                self.__conn.close()
            self.__conn = None
    #---------------------------------------------------------------------------
#-------------------------------------------------------------------------------