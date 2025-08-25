#-------------------------------------------------------------------------------
from ..engine       import MySqlEngine
from ..engine       import PostgreSqlEngine
from ..engine       import Sqlite3Engine
from ..common       import private
from ..common       import public
from ..config       import Config
from ..mapper       import Query
from ..errors       import EngineSetupError
#-------------------------------------------------------------------------------
class DDL:
    """
    Define Data Definition Language class
    """
    #---------------------------------------------------------------------------
    def __init__(self, query : str) -> None:
        """
        Initialize Data Definition Language class
        Args:
            query (str) : query text
        """
        self.__query = query
    #---------------------------------------------------------------------------
    @property
    @private
    def __sqlEngine(self) -> Sqlite3Engine | MySqlEngine | PostgreSqlEngine:
        """
        Setting SQL engine
        """
        engine = Config.sqlEngine
        if engine is None:
            raise EngineSetupError()
        return engine
    #---------------------------------------------------------------------------
    @public
    def execute(self) -> None:
        self.__sqlEngine.execute(Query(self.__query))
    #---------------------------------------------------------------------------
    @public
    def commit(self) -> None:
        self.__sqlEngine.commit()
#-------------------------------------------------------------------------------