#-------------------------------------------------------------------------------
from ..Base    import Base 
#-------------------------------------------------------------------------------
class DropTrigger(Base):
    """
    Define trigger deletion class
    """
    def __init__(
            self,
            tableName   : str,
            triggerName : str
        ) -> None:
        """
        Initialize trigger deletion object
        Args:
            tableName   (str) : table name
            triggerName (str) : trigger name
        """
        super().__init__(tableName)
        self.query = f"DROP TRIGGER {triggerName};"
#-------------------------------------------------------------------------------