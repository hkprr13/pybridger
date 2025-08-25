#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncCreateIndex(AsyncBase):
    """
    Define an asynchronous index creation class
    """
    def __init__(
            self,
            indexName : str,
            tableName : str,
            columns   : str
        ) -> None:
        """
        Initialize an asynchronous index creation class
        Args:
            indexName (str) : index name
            tableName (str) : table name
            columns   (str) : column
        """
        super().__init__(tableName)
        self.query = f"CREATE {indexName} ON {tableName} ({columns});"
#-------------------------------------------------------------------------------