#-------------------------------------------------------------------------------
from typing             import Any
from .IntegerType       import IntegerType
from ....common         import override
from ....common         import public
from ....mapper         import Query
#-------------------------------------------------------------------------------
class SmallInt(IntegerType):
    """
    Define 2-byte integer type class
    Supported SQL (MySQL, PostgreSQL)

    MySQL query      : "SMALLINT"
    Sqlite3 query    : "INTEGER"
    PostgreSQL query : "SMALLINT"
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize 2-byte integer type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self):
        self.query                : Any = Query("SMALLINT")
        self.storage              : Any =       2
        self.signedMaximum        : Any =  32,767
        self.signedMinimum        : Any = -32,768
        self.maximumUnsignedValue : Any =  65,535
        self.minimumUnsignedValue : Any =       0
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self):
        self.query                : Any = Query("INTEGER")
        self.storage              : Any = self.TEXTNOTSUPPORTED
        self.signedMaximum        : Any = self.TEXTNOTSUPPORTED
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self):
        self.query                : Any = Query("SMALLINT")
        self.storage              : Any =       2
        self.signedMaximum        : Any =  32,767
        self.signedMinimum        : Any = -32,768
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------