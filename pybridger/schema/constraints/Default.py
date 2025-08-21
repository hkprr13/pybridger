#-------------------------------------------------------------------------------
from .Constraints   import Constraints  
from ...common      import override     
from ...common      import private     
from ...mapper      import Query       
#-------------------------------------------------------------------------------
class Default(Constraints):
    """
    Defined default constraints
    """
    def __init__(self, value: str | int | float | bool):
        """
        Initalize default constraints object
        Args:
            value (str | int | float | bool) : defalut value
        """
        self.__value = value
    #---------------------------------------------------------------------------
    @private
    def __buildDefaultQuery(self) -> Query:
        """
        private method
        Build query for default 
        Returns:
            Query : query object
        """
        if isinstance(self.__value, str):
            return Query(f"DEFAULT '{self.__value}'")
        elif isinstance(self.__value, bool):
            if self.__value:
                return Query("DEFAULT TRUE")
            else:
                return Query("DEFAULT FALSE")
        else:
            return Query(f"DEFAULT {self.__value}")
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query(self.__buildDefaultQuery())
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query(self.__buildDefaultQuery())
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query(self.__buildDefaultQuery())
#-------------------------------------------------------------------------------