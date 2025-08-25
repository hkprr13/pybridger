#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase 
#-------------------------------------------------------------------------------
class AsyncDropTable(AsyncBase):
    """
    Define the table deletion object
    """
    def __init__(self, tableName: str):
        """
        Initialize the table deletion class
        Args:
            tableName (str) : table name
        """
        super().__init__(tableName)
        self.query = f"DROP TABLE {self.tableName}"
#-------------------------------------------------------------------------------