#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class VarChar(StringType):
    """
    Define variable-length string data type class
    Supported SQL (MySQL, Sqlite3, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, length : int) -> None:
        """
        Initialize variable-length string data type object
        Args:
            length (int) : length 
        Examples:
            ```
            dataType = VarChar(16)
            ```
        """
        super().__init__()
        self.length = length
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query  : Any = Query(f"VARCHAR({self.length})")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query  : Any = Query(f"VARCHAR({self.length})")
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query  : Any = Query(f"VARCHAR({self.length})")
#-------------------------------------------------------------------------------