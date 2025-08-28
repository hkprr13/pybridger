#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import public
from ....mapper     import Query
#-------------------------------------------------------------------------------
class TinyBlob(StringType):
    """
    Define 255B binary type class
    Supported SQL (MySQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize 255B binary type object
        Args:
        
        Examples:
            ```
            dataType = TinyBlob()
            ```
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query : Any = Query("TINYBLOB")
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