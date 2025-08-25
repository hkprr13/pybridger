#-------------------------------------------------------------------------------
from ..Base     import Base
from ...config  import Config
from ...errors  import EngineUndefinedError
#-------------------------------------------------------------------------------
class DropIndex(Base):
    """
    Define the index deletion class    
    """
    def __init__(
            self,
            tableName : str,
            indexName : str
        ) -> None:
        """
        Initialize the index deletion object
        Args:
            tableName (str) : table name
            indexName (str) : index name
        """
        super().__init__(tableName)
        self.__indexName = indexName
        self.query = self.__buildQuery()
    #--------------------------------------------------------------------------
    def __buildQuery(self) -> str:
        """
        Build query
        Returns:
            str : query
        Raises:
            Exceptin : engine is un defined
        """
        if self.sqlEngine == Config.sqlite3Engine:
            return f"DROP INDEX {self.__indexName};"
        elif self.sqlEngine == Config.mySqlEngine:
            return f"DROP INDEX {self.__indexName} ON {self.tableName};"
        else:
            raise EngineUndefinedError()
#-------------------------------------------------------------------------------