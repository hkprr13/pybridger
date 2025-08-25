#-------------------------------------------------------------------------------
from ..Base    import Base
#-------------------------------------------------------------------------------
class AlterTableAddColumn(Base):
    """
    Define a class to add columns to the table
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName   : str,
            column      : str,
            dataType    : str,
            constraints : str,
        ) -> None:
        """
        Initialize the class that adds columns to the table
        Args:
            tableName   (str) : table name
            column      (str) : column name
            dataType    (str) : data type
            constraints (str) : constraints
        """
        super().__init__(tableName)
        self.query = f"ALTER TABLE {tableName} ADD " \
                   + f"{column} {dataType} {constraints};"
#-------------------------------------------------------------------------------