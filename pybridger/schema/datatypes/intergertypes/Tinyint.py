#-------------------------------------------------------------------------------
from typing             import Any
from .IntegerType       import IntegerType
from ....common         import override
from ....common         import public
from ....mapper         import Query
#-------------------------------------------------------------------------------
class TinyInt(IntegerType):
    """
    Define 1-byte integer type class
    Supported SQL (MySQL)

    MySQL query      : "TINYINT"
    Sqlite3 query    : "INTEGER"
    PostgreSQL query : "INTEGER"
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize 1-byte integer type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query                : Any = Query("TINYINT")
        self.storage              : Any =    1
        self.signedMaximum        : Any =  127
        self.signedMinimum        : Any = -128
        self.maximumUnsignedValue : Any =  255
        self.minimumUnsignedValue : Any =    0
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self) -> None:
        self.query                : Any = Query("INTEGER")
        self.storage              : Any = self.TEXTNOTSUPPORTED
        self.signedMaximum        : Any = self.TEXTNOTSUPPORTED
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self) -> None:
        self.query                : Any = Query("INTEGER")
        self.storage              : Any = self.TEXTNOTSUPPORTED
        self.signedMaximum        : Any = self.TEXTNOTSUPPORTED
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------