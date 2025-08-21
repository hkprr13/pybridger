#-------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override
from ...mapper      import Query
#-------------------------------------------------------------------------------
class NotNull(Constraint):
    """
    Defined not null constraint
    """
    #---------------------------------------------------------------------------
    def __init__(self):
        """
        Intialize not null constraint object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query("NOT NULL")
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query("NOT NULL")
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query("NOT NULL")
#-------------------------------------------------------------------------------
