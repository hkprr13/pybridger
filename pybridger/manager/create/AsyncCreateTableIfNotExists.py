#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncCreateTableIfNotExists(AsyncBase):
    """
    Define an asynchronous table creation class
    """
    def __init__(
            self,
            tableName : str,
            columns   : str
        ) -> None:
        """
        Initialize an asynchronous table creation class
        Args:
            tableName (str) : table name
            columns   (str) : The ... part of "CREATE TABLE (...);"
        """
        super().__init__(tableName)
        self.query = f"CREATE TABLE IF NOT EXISTS {tableName} ({columns});"
#-------------------------------------------------------------------------------