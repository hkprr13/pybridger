#-------------------------------------------------------------------------------
from ..Base    import Base
#-------------------------------------------------------------------------------
class DropIndexIfExists(Base):
    """
    Define the index deletion class. If the table exists
    """
    def __init__(
            self,
            tableName : str,
            indexName : str
        ) -> None:
        """
        Initialize the index deletion object. If the table exists
        Args:
            tableName (str) : table name
            indexName (str) : index name
        """
        super().__init__(tableName)
        self.query = f"DROP INDEX IF NOT EXISTS{indexName};"
#-------------------------------------------------------------------------------