#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class MediumBlob(StringType):
    """
    Define 16B binary type class
    Supported SQL (MySQL, Sqlite3)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize 16B binary type object
        Args:
        
        Examples:
            ```
            dataType = MediumBlob()
            ```
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query("MEDIUMBLOB")
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