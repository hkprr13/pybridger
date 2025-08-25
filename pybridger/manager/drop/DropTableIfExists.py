#-------------------------------------------------------------------------------
from ..Base     import Base
from ...common  import private
from ...config  import Config
from ...errors  import DatabaseUndefinedError
#-------------------------------------------------------------------------------
class DropTableIfExists(Base):
    """
    Define the table deletion object. If the table exists
    """
    def __init__(self, tableName: str):
        """
        Initialize the table deletion object. If the table exists
        Args:
            tableName (str) : table name
        """
        super().__init__(tableName)
        self.query = self.__buildQuery()
    #---------------------------------------------------------------------------
    @private
    def __buildQuery(self) -> str:
        """
        build query
        Returns:
            str : query
        Raises:
            DatabaseUndefinedError : Engine is un defined
        """
        if self.sqlEngine == Config.sqlite3Engine:
            return f"DROP TABLE IF NOT EXISTS {self.tableName}"
        elif self.sqlEngine == Config.mySqlEngine:
            return f"DROP TABLE IF NOT EXISTS {self.tableName}"
        else:
            raise DatabaseUndefinedError()
#-------------------------------------------------------------------------------