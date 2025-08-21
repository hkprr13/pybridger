#-------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override
from ...mapper      import Query
#-------------------------------------------------------------------------------
class Unique(Constraint):
    """
    Defined unique constraint
    """
    def __init__(self):
        """
        Initialize unique constraint object
        """
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query("UNIQUE")
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query("UNIQUE")
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query("UNIQUE")
#-------------------------------------------------------------------------------
