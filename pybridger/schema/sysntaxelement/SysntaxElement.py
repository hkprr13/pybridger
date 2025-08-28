#-------------------------------------------------------------------------------
from typing         import Any
from ...errors      import EngineUndefinedError
from ...errors      import EngineSetupError
from ...common      import public
from ...config      import Config
#-------------------------------------------------------------------------------
class SysntaxElement:
    TEXTNOTSUPPORTED: str = "Not supported"
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        # Use Any here, subclasses will define the specific type
        self.query : Any
    #---------------------------------------------------------------------------
    @public
    def checkSettingEngine(self):
        # If synchronous and asynchronous engines are not set
        if Config.sqlEngine is None and Config.asyncSqlEngine is None:
            raise EngineUndefinedError()
        # Synchronous engine is set, but asynchronous engine is not set
        elif Config.asyncSqlEngine is None and Config.sqlEngine is not None:
            self.sqlEngine = Config.sqlEngine
        # Synchronous engine is not set and asynchronous engine is set
        elif Config.sqlEngine is None and Config.asyncSqlEngine is not None:
            self.sqlEngine = Config.asyncSqlEngine
        else:
            raise EngineSetupError()
    #---------------------------------------------------------------------------
    @public
    def mysql(self) -> None:
        """
        MySQL
        """
    #---------------------------------------------------------------------------
    @public
    def sqlite3(self) -> None:
        """
        Sqlite3
        """
    #---------------------------------------------------------------------------
    @public
    def postgresql(self) -> None:
        """
        PostgreSQL
        """
    #---------------------------------------------------------------------------
    @public
    def toQuery(self) -> Any:
        # Check engine
        self.checkSettingEngine()
        name = self.sqlEngine.__name__
        # MySQL
        if  name == "MySqlEngine":
            self.mysql()
        # Sqlite3
        elif name == "Sqlite3Engine":
            self.sqlite3()
        # PostgreSQL
        elif name == "PostgreSqlEngine":
            self.postgresql()
        # Other
        else:
            raise EngineUndefinedError()
        return self.query
#-------------------------------------------------------------------------------