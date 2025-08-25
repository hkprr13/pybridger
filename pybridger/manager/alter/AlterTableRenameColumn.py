#-------------------------------------------------------------------------------
from ..Base    import Base  
#-------------------------------------------------------------------------------
class AlterTableRenameColumn(Base):
    """
    Define a class for changing table column names
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            oldName   : str,
            newName   : str,
        ) -> None:
        """
        Initialize a class for changing table column names
        Args:
            tableName (str) : table name
            oldName   (str) : old name
            newName   (str) : new name
        """
        super().__init__(tableName)
        self.query = f"ALTER TABLE {tableName} " \
                   + f"RENAME COLUMN {oldName} TO {newName};"
#-------------------------------------------------------------------------------