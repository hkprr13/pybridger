#-------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override
from ...mapper      import Query
#-------------------------------------------------------------------------------
class Check(Constraint):
    """
    Defined check constraint class
    """
    def __init__(self, conditons : str) -> None:
        """
        Initialize check constraint object
        Args:
            condtions (str) : conditional expression by specify string
        Examples:
        ```
            Check('id >= 1')
        ```
        """
        self.__conditions = conditons
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query(f"CHECK ({self.__conditions})")
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query(f"CHECK ({self.__conditions})")
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query(f"CHECK ({self.__conditions})")
#-------------------------------------------------------------------------------