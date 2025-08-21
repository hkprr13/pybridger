#-------------------------------------------------------------------------------
from .DateTimeType      import DateTimeType
from ....common         import override
from ....common         import public
from ....mapper         import Query
#-------------------------------------------------------------------------------
class Date(DateTimeType):
    """
    Date type class
    Supported SQL (MySQL, PostgreSQL)
    """
    #---------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Initalize date type object
        """
        super().__init__()
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query  = Query("DATE")
        self.format = "YYYY-MM-DD"
        self.range  = "1000-01-01~9999-12-31"
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
        self.query  = Query("DATE")
        self.format = "YYYY-MM-DD"
        self.range  = "BC4713~AD5874897"
#-------------------------------------------------------------------------------