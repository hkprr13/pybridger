#-------------------------------------------------------------------------------
from ..Base         import Base 
#-------------------------------------------------------------------------------
class CreateTableIfNotExists(Base):
    """
    Define table creation class.
    """
    def __init__(
            self,
            tableName : str,
            columns   : str
        ) -> None:
        """
        Initialize table creation object
        Args:
            tableName (str) : Table name
            columns   (str) : The ... part of "CREATE TABLE (...);"
        """
        super().__init__(tableName)
        self.query = f"CREATE TABLE IF NOT EXISTS {tableName} ({columns});"
#-------------------------------------------------------------------------------