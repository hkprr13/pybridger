#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncDropViewIfExists(AsyncBase):
    """
    Define view deletion class. If the table exists
    """
    def __init__(
            self,
            tableName : str,
            viewName  : str
        ) -> None:
        """
        Initalize view deletion object. If the table exists
        Args:
            tableName (str) : table name
            viewName   (str) : view name
        """
        super().__init__(tableName)
        self.query = f"DROP VIEW IF NOT EXISTS {viewName};"
#-------------------------------------------------------------------------------