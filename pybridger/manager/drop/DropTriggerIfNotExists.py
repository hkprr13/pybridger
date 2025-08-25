#-------------------------------------------------------------------------------
from ..Base    import Base
#-------------------------------------------------------------------------------
class DropTriggerIfNotExists(Base):
    """
    Define trigger deletion class. If the table exists
    """
    def __init__(
            self,
            tableName   : str,
            triggerName : str
        ):
        """
        Initalize trigger deletion object. If the table exists
        Args:
            tableName   (str) : table name
            triggerName (str) : trigger name
        """
        super().__init__(tableName)
        self.query = f"DROP TRIGGER IF NOT EXISTS {triggerName};"
#-------------------------------------------------------------------------------