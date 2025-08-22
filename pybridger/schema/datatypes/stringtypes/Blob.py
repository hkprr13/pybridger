#-------------------------------------------------------------------------------
from typing         import Any
from .StringType    import StringType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Blob(StringType):
    """
    Define large binary type class
    Supported SQL (MySQL, Sqlite3)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize Large binary type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query("BLOB")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query  : Any = Query("BLOB")
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query  : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------