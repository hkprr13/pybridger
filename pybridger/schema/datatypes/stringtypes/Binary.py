#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Binary(StringType):
    """
    Define fixed-length binary data type class
    Supported SQL (MySQL, Sqlite3, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, length : int) -> None:
        """
        Initialize fixed-length binary data type object
        Args:
            length (int) : length
        Examples:
            ```
            dataType = Binary(16)
            ```
        """
        super().__init__()
        self.length = length
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query(f"BINARY({self.length})")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------