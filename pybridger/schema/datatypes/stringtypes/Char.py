#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import public
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Char(StringType):
    """
    Define fixed-length string data type
    Supported SQL (MySQL, Sqlite3, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, length : int) -> None:
        """
        Initialize a fixed-length string data type object
        Args:
            length (int) : String length
        Examples:
            ```
            Char(16)
            ```
        """
        super().__init__()
        self.length = length
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query : Any = Query(f"CHAR({self.length})")
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self) -> None:
        self.query : Any = Query(f"CHAR({self.length})")
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self) -> None:
        self.query : Any = Query(f"CHAR({self.length})")
#-------------------------------------------------------------------------------