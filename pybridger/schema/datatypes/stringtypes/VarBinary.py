#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import public
from ....mapper     import Query
#-------------------------------------------------------------------------------
class VarBinary(StringType):
    """
    Define variable-length binary data type class
    Supported SQL(MySQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self, length : int) -> None:
        """
        Initialize variable-length binary data type object
        Args:
            length (int) : length 
        Examples:
            ```
            dataType = VarBinary(16)
            ```
        """
        super().__init__()
        self.length = length
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query : Any = Query(f"VARBINARY({self.length})")
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