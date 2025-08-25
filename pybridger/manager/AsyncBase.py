#-------------------------------------------------------------------------------
from typing     import Any
from ..engine   import AsyncSqlite3Engine
from ..engine   import AsyncMySqlEngine
from ..engine   import AsyncPostgreSqlEngine
from ..common   import public
from ..config   import Config
from ..mapper   import Query
from ..errors   import EngineUndefinedError
#-------------------------------------------------------------------------------
class AsyncBase:
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
    def sqlEngine(
            self
        ) -> AsyncSqlite3Engine | AsyncMySqlEngine | AsyncPostgreSqlEngine:
        """
        Setting SQL engine
        Returns:
             Sqlite3Engine | MySqlEngine | PostgreSqlEngine : engine object
        """
        engine = Config.asyncSqlEngine
        if engine is None:
            raise EngineUndefinedError()
        return engine
    #---------------------------------------------------------------------------
    @public
    async def connect(self) -> None:
        """
        Connect 
        """    
        await self.sqlEngine.connect()
    #---------------------------------------------------------------------------        
    @public
    async def cursor(self) -> Any:
        """
        Cursor
        """
        return await self.sqlEngine.cursor()
    # #---------------------------------------------------------------------------
    @public
    async def execute(self) -> None:
        """
        Execute
        """
        await self.sqlEngine.execute(Query(self.query), self.value)
    #---------------------------------------------------------------------------
    @public
    async def executeAny(self) -> None:
        """
        Execute any
        """
        await self.sqlEngine.executeAny(Query(self.query), self.data)
    #---------------------------------------------------------------------------
    @public
    async def commit(self) -> None:
        """
        Commit transaction
        """
        await self.sqlEngine.commit()
    #---------------------------------------------------------------------------
    @public
    async def transaction(self) -> None:
        """
        Transaction
        """
        await self.sqlEngine.transaction()
    #---------------------------------------------------------------------------
    @public
    async def rollback(self) -> None:
        """
        Rollback
        """
        await self.sqlEngine.rollback()
#-------------------------------------------------------------------------------