#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncDropTableIfExists(AsyncBase):
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
        self.query = f"DROP TABLE IF NOT EXISTS {self.tableName}"
#-------------------------------------------------------------------------------