#-------------------------------------------------------------------------------
from .DateTimeType      import DateTimeType
from ....common         import override
from ....common         import public
from ....mapper         import Query
#-------------------------------------------------------------------------------
class Year(DateTimeType):
    """
    年型
    サポートされているSQL(MySQL)
    """
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query  = Query(f"YEAR")
        self.format = "YYYY"
        self.range  = "1901~2155"
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self) -> None:
        self.query  = self.TEXTNOTSUPPORTED
        self.format = self.TEXTNOTSUPPORTED
        self.range  = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self) -> None:
        self.query  = self.TEXTNOTSUPPORTED
        self.format = self.TEXTNOTSUPPORTED
        self.range  = self.TEXTNOTSUPPORTED
#-------------------------------------------------------------------------------