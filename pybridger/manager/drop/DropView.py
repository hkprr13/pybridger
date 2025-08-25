#-------------------------------------------------------------------------------
from ..Base    import Base
#-------------------------------------------------------------------------------
class DropView(Base):
    """
    Define view deletion class
    """
    def __init__(
            self,
            tableName : str,
            viewName  : str
        ) -> None:
        """
        Initalize view deletion object
        Args:
            tableName (str) : table name
            viewName   (str) : view name
        """
        super().__init__(tableName)
        self.query = f"DROP VIEW {viewName};"
#-------------------------------------------------------------------------------