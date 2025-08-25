#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncDropView(AsyncBase):
    """
    Define view deletion class
    """
    def __init__(
            self,
            tableName : str,
            viewName  : str
        ) -> None:
        """
        Initalize view deletion object
        Args:
            tableName (str) : table name
            viewName   (str) : view name
        """
        super().__init__(tableName)
        self.query = f"DROP VIEW {viewName};"
#-------------------------------------------------------------------------------