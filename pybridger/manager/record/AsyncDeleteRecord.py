#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncDeleteRecord(AsyncBase):
    """
    Define a record deletion class
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            columns   : str,
            values    : tuple
        ) -> None:
        """
        Initialize a record deletion object
        """
        super().__init__(tableName)
        query = f"DELETE FROM {self.tableName} WHERE {columns}"
        self.query = query.replace(
            "?", self.sqlEngine.PLACEHOLDER
        )
        self.value = values
#-------------------------------------------------------------------------------