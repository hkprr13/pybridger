#-------------------------------------------------------------------------------
from typing         import Any
from .LogicalType   import LogicalType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Boolean(LogicalType):
    """
    Define boolen type class
    Supported SQL (MySQL, Sqlite3, PostgreSQL)

    MySQL query      : "BOOLEAN"
    Sqlite3 query    : "BOOLEAN"
    PostgreSQL query : "BOOLEAN"
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize boolen type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query("BOOLEAN")
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query : Any = Query("BOOLEAN")
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query : Any = Query("BOOLEAN")
#-------------------------------------------------------------------------------