#-------------------------------------------------------------------------------
from typing             import Any
from .IntegerType       import IntegerType
from ....common         import override
from ....common         import private
from ....mapper         import Query
#-------------------------------------------------------------------------------
class Integer(IntegerType):
    """
    Define 3-byte integer type
    Supported SQL (MySQL, Sqlite3, PostgreSQL)

    MySQL query      : "INT"
    Sqlite3 query    : "INTEGER"
    PostgreSQL query : "INT
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize integer type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query                : Any = Query("INT")
        self.storage              : Any =              4
        self.signedMaximum        : Any =  2_147_483_647
        self.signedMinimum        : Any = -2_147_483_648
        self.maximumUnsignedValue : Any =  4_294_967_295
        self.minimumUnsignedValue : Any =              0
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query                : Any = Query("INTEGER")
        self.storage              : Any =  "1~8"
        self.signedMaximum        : Any = -9_223_372_036_854_775_808
        self.signedMinimum        : Any =  9_223_372_036_854_775_807
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query                : Any = Query("INT")
        self.storage              : Any =              4
        self.signedMaximum        : Any =  2_147_483_647
        self.signedMinimum        : Any = -2_147_483_648
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------