#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Enum(StringType):
    """
    Define enumerated types class
    Supported SQL (MySQL, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, *args) -> None:
        """
        Initialize Enumerated types object
        Args:
            args : List values
        Examples:
            ```
            dataType = Enum('a', 'b', 'c', 'd', 'e')
            ```
        """
        super().__init__()
        self.__args = args
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query(f"ENUM{self.__args}")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query : Any = Query(f"ENUM{self.__args}")
#-------------------------------------------------------------------------------