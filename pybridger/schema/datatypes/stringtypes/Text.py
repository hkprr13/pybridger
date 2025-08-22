#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Text(StringType):
    """
    Define text type class
    Supported SQL (MySQL, Sqlite3, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize text type object
        Args:
        
        Examples:
            ```
            dataType = Text()
            ```
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query("TEXT")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query : Any = Query("TEXT")
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query : Any = Query("TEXT")
#-------------------------------------------------------------------------------