#-------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override
from ...mapper      import Query
#-------------------------------------------------------------------------------
class Check(Constraint):
    """
    Defined check constraint class
    """
    def __init__(self, conditons : str | None) -> None:
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
    def __buildCheckQuery(self) -> Query:
        if self.__conditions:
            return Query(f"CHECK ({self.__conditions})")
        else:
            return Query("")
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query = self.__buildCheckQuery()
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query = self.__buildCheckQuery()
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query = self.__buildCheckQuery()
#-------------------------------------------------------------------------------