#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class TinyText(StringType):
    """
    Define Tiny text type class
    Supported SQL(MySQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize Tiny text type object
        Args:
        
        Examples:
            ```
            dataType = TinyText()
            ```
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query("TINYTEXT")
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