#-------------------------------------------------------------------------------
from ..Base    import Base
#-------------------------------------------------------------------------------
class AlterTableDropColumn(Base):
    """
    Define a class to delete columns from the table
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName  : str,
            columnName : str
        ) -> None:
        """
        Initialize a class to delete columns from the table
        Args:
            tableName  (str) : table name
            columnName (str) : column name
        """
        super().__init__(tableName)
        self.query = f"ALTER TABLE {tableName} DROP COLUMN {columnName};"
#-------------------------------------------------------------------------------