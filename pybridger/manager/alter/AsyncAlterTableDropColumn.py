#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncAlterTableDropColumn(AsyncBase):
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
        Initialize a class to delete columns from the table.
        Args:
            tableName (str)  : table name
            columnNmae (str) : column name
        """
        super().__init__(tableName)
        self.query = f"ALTER TABLE {tableName} DROP COLUMN {columnName};"
#-------------------------------------------------------------------------------