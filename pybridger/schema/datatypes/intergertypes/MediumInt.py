#-------------------------------------------------------------------------------
from typing             import Any
from .IntegerType       import IntegerType
from ....common         import override
from ....common         import private
from ....mapper         import Query
#-------------------------------------------------------------------------------
class MediumnInt(IntegerType):
    """
    Define 3-byte integer type
    Supported SQL (MySQL)
    MySQL query      : "MEDIUMINT"
    Sqlite3 query    : "INTEGER"
    PostgreSQL query : "INTEGER"
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initialize 3-byte integer type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self):
        self.query                : Any = Query("MEDIUMINT")
        self.storage              : Any =          3
        self.signedMaximum        : Any =  8_388_607
        self.signedMinimum        : Any = -8_388_608
        self.maximumUnsignedValue : Any = 16_777_215
        self.minimumUnsignedValue : Any =          0
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self):
        self.query                : Any = Query("INTEGER")
        self.storage              : Any = self.TEXTNOTSUPPORTED
        self.signedMaximum        : Any = self.TEXTNOTSUPPORTED
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self):
        self.query                : Any = Query("INTEGER")
        self.storage              : Any = self.TEXTNOTSUPPORTED
        self.signedMaximum        : Any = self.TEXTNOTSUPPORTED
        self.signedMinimum        : Any = self.TEXTNOTSUPPORTED
        self.maximumUnsignedValue : Any = self.TEXTNOTSUPPORTED
        self.minimumUnsignedValue : Any = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------