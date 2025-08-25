#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncDropTrigger(AsyncBase):
    """
    Define trigger deletion class
    """
    def __init__(
            self,
            tableName   : str,
            triggerName : str
        ) -> None:
        """
        Initalize trigger deletion object
        Args:
            tableName   (str) : table name
            triggerName (str) : trigger name
        """
        super().__init__(tableName)
        self.query = f"DROP TRIGGER {triggerName};"
#-------------------------------------------------------------------------------