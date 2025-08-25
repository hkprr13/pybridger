#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncDropIndex(AsyncBase):
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
        self.query = f"DROP INDEX {indexName};"
#-------------------------------------------------------------------------------