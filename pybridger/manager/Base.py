#-------------------------------------------------------------------------------
from typing     import Any
from ..common   import public
from ..config   import Config
from ..mapper   import Query
from ..errors   import EngineUndefinedError
#-------------------------------------------------------------------------------
class Base:
    """
    Define a base class for the database operation manager class    
    """
    def __init__(self, tableName : str) -> None:
        """
        Initialize a base class for the database operation manager object
        """
        self.tableName = tableName
        self.query : str
        self.value : tuple
        self.data  : list[tuple[str]]
    #---------------------------------------------------------------------------
    @property
    @public
    def sqlEngine(self) -> Any:
        """
        Setting SQL engine
        Returns:
             Sqlite3Engine | MySqlEngine | PostgreSqlEngine : engine object
        """
        engine = Config.sqlEngine
        if engine is None:
            raise EngineUndefinedError()
        return engine
    #---------------------------------------------------------------------------
    @public
    def connect(self) -> None:
        """
        Connect 
        """
        self.sqlEngine.connect()
    #---------------------------------------------------------------------------        
    @public
    def cursor(self) -> Any:
        """
        Cursor
        """
        return self.sqlEngine.cursor()
    #---------------------------------------------------------------------------
    @public
    def execute(self) -> None:
        """
        Execute
        """
        self.sqlEngine.execute(Query(self.query), self.value)
    #---------------------------------------------------------------------------
    @public
    def executeAny(self) -> None:
        """
        Execute any
        """
        self.sqlEngine.executeAny(Query(self.query), self.data)
    #---------------------------------------------------------------------------
    @public
    def commit(self) -> None:
        """
        Commit transaction
        """
        self.sqlEngine.commit()
    #---------------------------------------------------------------------------
    @public
    def close(self) -> None:
        """
        Connection close
        """
        self.sqlEngine.close()
    #---------------------------------------------------------------------------
    @public
    def transaction(self) -> None:
        """
        Transaction
        """
        self.sqlEngine.transaction()
    #---------------------------------------------------------------------------
    @public
    def rollback(self) -> None:
        """
        Rollback
        """
        self.sqlEngine.rollback()
#-------------------------------------------------------------------------------