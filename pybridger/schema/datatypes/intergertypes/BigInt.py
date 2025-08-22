#-------------------------------------------------------------------------------
from typing             import Any
from .IntegerType       import IntegerType
from ....common         import override
from ....common         import private
from ....mapper         import Query
#-------------------------------------------------------------------------------
class BigInt(IntegerType):
    """
    Define 8-byte integer type
    Supported SQL (MySQL, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize 8-byte integer type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query                : Any = Query("BIGINT")
        self.storage              : Any =                          8
        self.signedMaximum        : Any =  9_223_372_036_854_775_807
        self.signedMinimum        : Any = -9_223_372_036_854_775_808
        self.maximumUnsignedValue : Any =                          0
        self.minimumUnsignedValue : Any = 18_446_744_073_709_551_615
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query                : Any = self.TEXTNOTSUPPORTED
        self.storage              : Any = self.TEXTNOTSUPPORTED
        self.signedMaximum        : Any = self.TEXTNOTSUPPORTED
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.storage              : Any =                          8
        self.signedMaximum        : Any =  9_223_372_036_854_775_807
        self.signedMinimum        : Any = -9_223_372_036_854_775_808
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------