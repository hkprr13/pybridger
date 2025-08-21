#-------------------------------------------------------------------------------
from .DateTimeType      import DateTimeType
from ....common         import override
from ....common         import private
from ....common         import public
from ....mapper         import Query
#-------------------------------------------------------------------------------
class DateTime(DateTimeType):
    """
    Date time type
    Supported SQL (MySQL)
    """
    def __init__(self, precision : int = 0) -> None:
        super().__init__()
        self.precision = precision
    #---------------------------------------------------------------------------
    @private
    def __setMysqlFormat(self) -> str:
        """
        Setting MySQL format
        Returns:
            str : format
        """
        __format = "YYYY-MM-DD HH:MM:SS"
        if self.precision:
            return __format
        else:
            __format += "."
            __format += "f" * self.precision
            return __format
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query  = Query(f"DATETIME({self.precision})")
        self.format = self.__setMysqlFormat()
        self.range  = "1000-01-01 00:00:00~9999-12-31 23:59:59"
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