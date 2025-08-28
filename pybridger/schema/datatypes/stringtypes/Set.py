#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import public
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Set(StringType):
    """
    Define multiple selection type class
    Supported SQL (MySQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, *args) -> None:
        """
        Initialize multiple selection type object
        Args:
            args : list values
        Examples:
            ```
            dataType = Set()
            ```
        """
        super().__init__()
        self.__args = args
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query : Any = Query(f"SET{self.__args}")
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------