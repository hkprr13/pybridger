#-------------------------------------------------------------------------------
from ..Base    import Base
#-------------------------------------------------------------------------------
class DropTable(Base):
    """
    Define the table deletion object
    """
    def __init__(self, tableName: str) -> None:
        """
        Initialize the table deletion class
        Args:
            tableName (str) : table name
        """
        super().__init__(tableName)
        self.query = f"DROP TABLE {self.tableName}"
#-------------------------------------------------------------------------------