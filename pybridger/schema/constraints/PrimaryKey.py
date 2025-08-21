#-------------------------------------------------------------------------------
from .Constraint    import Constraint
from ...common      import override 
from ...common      import public
from ...mapper      import Query
#-------------------------------------------------------------------------------
class PrimaryKey(Constraint):
    """
    Defined primary key constraint class
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize primary key constraint object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @public
    def __buildPrimaryKeyQuery(self) -> Query:
        """
        private method
        Build query for primary key
        Returns:
            Query : query
        """
        return Query("PRIMARY KEY")
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = self.__buildPrimaryKeyQuery()
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = self.__buildPrimaryKeyQuery()
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = self.__buildPrimaryKeyQuery()
#-------------------------------------------------------------------------------
