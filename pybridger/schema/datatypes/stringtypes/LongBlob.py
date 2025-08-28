#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import public
from ....mapper     import Query
#-------------------------------------------------------------------------------
class LongBlob(StringType):
    """
    Define 4GB binary type class 
    Supported SQL (MySQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize 4GB binary type object
        Args:
        
        Examples:
            ```
            dataType = LongBlob()
            ```
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query : Any = Query("LONGBLOB")
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