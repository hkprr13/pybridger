#-------------------------------------------------------------------------------
from ..Base         import Base 
#-------------------------------------------------------------------------------
class CreateTable(Base):
    """
    Define table creation class.
    Even if it exists
    """
    def __init__(
            self,
            tableName : str,
            columns   : str
        ) -> None:
        """
        Initialize table creation object
        Args;
            tableName (str) : table name
            columns   (str) : The ... part of "CREATE TABLE (...);"
        """
        super().__init__(tableName)
        self.query = f"CREATE TABLE {tableName} ({columns});"
#-------------------------------------------------------------------------------